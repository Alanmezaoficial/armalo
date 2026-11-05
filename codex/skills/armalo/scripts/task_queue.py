"""Read-only task selection for both supported blueprint formats. MIT, Alanmeza.ai 2026."""
import argparse
import json
from pathlib import Path


def inspect_queue(document, task_id=None):
    tasks = document if isinstance(document, list) else document.get("tasks") if isinstance(document, dict) else None
    if not isinstance(tasks, list) or not tasks:
        raise ValueError("Expected a nonempty task array or an object containing tasks")
    by_id = {}
    for task in tasks:
        if not isinstance(task, dict) or not isinstance(task.get("id"), str) or not task["id"] or task["id"] in by_id:
            raise ValueError("Missing, invalid or duplicate task ID")
        by_id[task["id"]] = task
        if task.get("status") not in {"pending", "in_progress", "done", "completed", "deferred"}:
            raise ValueError("Unknown task status: " + task["id"])

    def dependencies(task):
        if "depends_on" in task and "dependencies" in task and task["depends_on"] != task["dependencies"]:
            raise ValueError("Conflicting dependency fields: " + task["id"])
        deps = task.get("depends_on", task.get("dependencies", []))
        if not isinstance(deps, list) or any(not isinstance(d, str) or d not in by_id for d in deps):
            raise ValueError("Unknown or invalid dependency: " + task["id"])
        return deps

    visiting, visited = set(), set()

    def visit(task_id):
        if task_id in visiting:
            raise ValueError("Dependency cycle: " + task_id)
        if task_id in visited:
            return
        visiting.add(task_id)
        for dep in dependencies(by_id[task_id]):
            visit(dep)
        visiting.remove(task_id)
        visited.add(task_id)

    for task in tasks:
        visit(task["id"])
    done = {"done", "completed"}
    queue = [{"id": task["id"], "title": task.get("title", ""), "status": task["status"],
              "blocked_by": [d for d in dependencies(task) if by_id[d]["status"] not in done]} for task in tasks]
    active = [task for task in tasks if task["status"] == "in_progress"]
    if len(active) > 1:
        raise ValueError("Multiple interrupted tasks; resolve active work before selecting")
    if task_id is not None:
        if task_id not in by_id:
            raise ValueError("Task does not exist: " + task_id)
        selected, state = by_id[task_id], "requested"
    elif active:
        selected, state = active[0], "resuming"
    else:
        selected = next((task for task, row in zip(tasks, queue) if task["status"] == "pending" and not row["blocked_by"]), None)
        state = "ready" if selected else "complete" if all(task["status"] in done for task in tasks) else "blocked"
    return {"state": state, "task": selected, "queue": queue, "read_only": True}


def main():
    parser = argparse.ArgumentParser(description="Inspect a task queue without changing it or executing verify commands")
    parser.add_argument("bundle", help="Bundle directory or tasks.json")
    parser.add_argument("--listar", "--list", action="store_true", help="Show the whole queue")
    parser.add_argument("--tarea", "--task", dest="task_id", help="Show one task")
    args = parser.parse_args()
    source = Path(args.bundle)
    if source.is_dir():
        source = source / "tasks.json"
    try:
        document = json.loads(source.read_text(encoding="utf-8-sig"))
        result = inspect_queue(document, args.task_id)
        if args.listar:
            result = {k: v for k, v in result.items() if k != "task"}
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError) as exc:
        parser.exit(2, str(exc) + "\n")


if __name__ == "__main__":
    main()
