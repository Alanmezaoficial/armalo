import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

HELPER = Path(__file__).resolve().parents[1] / "codex/skills/armalo/scripts/task_queue.py"
spec = importlib.util.spec_from_file_location("queue_helper", HELPER)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_existing_codex_schema_preserves_deferred_gate():
    doc = {"schema_version": 1, "tasks": [{"id": "1", "status": "completed"}, {"id": "2", "status": "deferred", "depends_on": ["1"]}, {"id": "3", "status": "pending", "depends_on": ["2"]}]}
    assert module.inspect_queue(doc)["state"] == "blocked"


def test_original_schema_selects_first_ready_in_file_order():
    tasks = [{"id": "1", "status": "done"}, {"id": "2", "status": "pending", "dependencies": ["1"]}, {"id": "3", "status": "pending", "dependencies": []}]
    assert module.inspect_queue(tasks)["task"]["id"] == "2"


def test_interrupted_task_precedes_other_ready_work():
    tasks = [{"id": "1", "status": "pending"}, {"id": "2", "status": "in_progress"}]
    assert module.inspect_queue(tasks)["state"] == "resuming"
    assert module.inspect_queue(tasks)["task"]["id"] == "2"


@pytest.mark.parametrize("tasks", [
    [{"id": "1", "status": "pending", "dependencies": ["missing"]}],
    [{"id": "1", "status": "pending", "dependencies": ["2"]}, {"id": "2", "status": "pending", "dependencies": ["1"]}],
    [{"id": "1", "status": "pending"}, {"id": "1", "status": "done"}],
    [{"id": "1", "status": "mystery"}],
    [{"id": "1", "status": "in_progress"}, {"id": "2", "status": "in_progress"}],
    [{"id": "1", "status": "pending", "depends_on": [], "dependencies": ["1"]}],
])
def test_ambiguous_or_corrupt_queues_are_rejected(tasks):
    with pytest.raises(ValueError):
        module.inspect_queue(tasks)


def test_cli_does_not_write_or_run_verify(tmp_path):
    source = tmp_path / "tasks.json"
    source.write_text(json.dumps([{"id": "1", "status": "pending", "verify": ["this command must never run"]}]), encoding="utf8")
    before = source.read_bytes()
    run = subprocess.run([sys.executable, "-B", str(HELPER), str(source)], capture_output=True, text=True, check=True)
    assert json.loads(run.stdout)["task"]["id"] == "1"
    assert before == source.read_bytes()
