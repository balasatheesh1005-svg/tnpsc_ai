import json
import os
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional, Tuple


class PipelineState(str, Enum):
    DISCOVERED = "DISCOVERED"
    NOTES_READY = "NOTES_READY"
    BLUEPRINT_READY = "BLUEPRINT_READY"
    PART_1_RUNNING = "PART_1_RUNNING"
    PART_1_COMPLETE = "PART_1_COMPLETE"
    PART_2A_RUNNING = "PART_2A_RUNNING"
    PART_2A_COMPLETE = "PART_2A_COMPLETE"
    PART_2B_RUNNING = "PART_2B_RUNNING"
    PART_2B_COMPLETE = "PART_2B_COMPLETE"
    CORE_COMPLETE = "CORE_COMPLETE"
    PART_3_RUNNING = "PART_3_RUNNING"
    PART_3_COMPLETE = "PART_3_COMPLETE"
    AUTO_VALIDATED = "AUTO_VALIDATED"
    REPAIR_REQUIRED = "REPAIR_REQUIRED"
    SEMANTIC_AUDIT = "SEMANTIC_AUDIT"
    SEMANTIC_AUDIT_COMPLETE = "SEMANTIC_AUDIT_COMPLETE"
    UI_TEST = "UI_TEST"
    UI_TEST_COMPLETE = "UI_TEST_COMPLETE"
    PRODUCTION_READY = "PRODUCTION_READY"
    TOPIC_ALREADY_RUNNING = "TOPIC_ALREADY_RUNNING"


class TopicLock:
    """
    Ensures concurrency safety: prevents two generation processes from running
    the same topic simultaneously.
    """

    def __init__(self, topic_id: str, status_dir: str = "data/pipeline_status", timeout_seconds: int = 1800):
        self.topic_id = topic_id
        self.status_dir = status_dir
        self.timeout_seconds = timeout_seconds
        os.makedirs(self.status_dir, exist_ok=True)
        self.lock_path = os.path.join(self.status_dir, f"{self.topic_id}.lock")
        self._acquired = False

    def is_locked(self) -> Tuple[bool, str]:
        if not os.path.exists(self.lock_path):
            return False, ""
        try:
            with open(self.lock_path, "r", encoding="utf-8") as f:
                lock_info = json.load(f)
            lock_pid = lock_info.get("pid")
            lock_time = lock_info.get("timestamp")
            lock_age = (datetime.now() - datetime.fromisoformat(lock_time)).total_seconds() if lock_time else 9999
            if lock_age < self.timeout_seconds:
                return True, f"TOPIC_ALREADY_RUNNING (PID: {lock_pid}, active for {int(lock_age)}s)"
            else:
                # Stale lock
                return False, ""
        except Exception:
            return False, ""

    def acquire(self) -> Tuple[bool, str]:
        locked, msg = self.is_locked()
        if locked:
            return False, msg

        lock_data = {
            "topic_id": self.topic_id,
            "pid": os.getpid(),
            "timestamp": datetime.now().isoformat(),
        }
        tmp_lock = f"{self.lock_path}.tmp"
        try:
            with open(tmp_lock, "w", encoding="utf-8") as f:
                json.dump(lock_data, f, indent=2)
            os.replace(tmp_lock, self.lock_path)
            self._acquired = True
            return True, "Lock acquired successfully"
        except Exception as e:
            return False, f"Failed to acquire lock: {e}"

    def release(self) -> None:
        if os.path.exists(self.lock_path):
            try:
                os.remove(self.lock_path)
            except Exception:
                pass
        self._acquired = False

    def __enter__(self):
        success, msg = self.acquire()
        if not success:
            raise RuntimeError(msg)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()


class PipelineCheckpointManager:
    """
    Manages persistent machine-readable checkpoints for the Nova AI Content Engine.
    Permits resuming midway without regenerating already-completed batches.
    Utilizes atomic writes to prevent partially-written or corrupted state files.
    """

    def __init__(self, topic_id: str, display_title: str = "", status_dir: str = "data/pipeline_status"):
        self.topic_id = topic_id
        self.display_title = display_title or topic_id
        self.status_dir = status_dir
        os.makedirs(self.status_dir, exist_ok=True)
        self.checkpoint_path = os.path.join(self.status_dir, f"{self.topic_id}.json")

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.checkpoint_path):
            return self._default_state()
        try:
            with open(self.checkpoint_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if "parts" not in data:
                data["parts"] = self._default_parts()
            return data
        except Exception:
            return self._default_state()

    def _default_parts(self) -> Dict[str, Dict[str, Any]]:
        return {
            "part1": {"status": "PENDING", "count": 0, "validated": False},
            "part2a": {"status": "PENDING", "count": 0, "validated": False},
            "part2b": {"status": "PENDING", "count": 0, "validated": False},
            "part3": {"status": "PENDING", "count": 0, "validated": False},
        }

    def _default_state(self) -> Dict[str, Any]:
        return {
            "topic": self.display_title,
            "topic_id": self.topic_id,
            "state": PipelineState.DISCOVERED.value,
            "auto_chain": True,
            "parts": self._default_parts(),
            "core_count": 0,
            "grand_test_count": 0,
            "overall_count": 0,
            "repair_cycles": 0,
            "notes": "",
            "last_updated": datetime.now().isoformat(),
        }

    def save(
        self,
        state: PipelineState,
        parts: Optional[Dict[str, Dict[str, Any]]] = None,
        core_count: Optional[int] = None,
        grand_test_count: Optional[int] = None,
        repair_cycles: int = 0,
        notes: str = "",
        extra_meta: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        current = self.load()
        updated_parts = parts if parts is not None else current.get("parts", self._default_parts())

        c_count = core_count
        if c_count is None:
            c_count = sum(p.get("count", 0) for k, p in updated_parts.items() if k != "part3")

        gt_count = grand_test_count
        if gt_count is None:
            gt_count = updated_parts.get("part3", {}).get("count", 0)

        status_data = {
            "topic": self.display_title or current.get("topic", self.topic_id),
            "topic_id": self.topic_id,
            "state": state.value if isinstance(state, PipelineState) else str(state),
            "auto_chain": True,
            "parts": updated_parts,
            "core_count": c_count,
            "grand_test_count": gt_count,
            "overall_count": c_count + gt_count,
            "repair_cycles": repair_cycles,
            "notes": notes,
            "last_updated": datetime.now().isoformat(),
        }
        if extra_meta:
            status_data.update(extra_meta)

        # Atomic write
        tmp_path = f"{self.checkpoint_path}.tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(status_data, f, indent=2, ensure_ascii=False)
        os.replace(tmp_path, self.checkpoint_path)

        return status_data

    def set_state(self, state: PipelineState, notes: str = "") -> Dict[str, Any]:
        data = self.load()
        return self.save(
            state=state,
            parts=data.get("parts"),
            core_count=data.get("core_count"),
            grand_test_count=data.get("grand_test_count"),
            repair_cycles=data.get("repair_cycles", 0),
            notes=notes or data.get("notes", ""),
        )

    def get_state(self) -> PipelineState:
        data = self.load()
        try:
            return PipelineState(data.get("state", PipelineState.DISCOVERED.value))
        except ValueError:
            return PipelineState.DISCOVERED

    def update_part_status(self, part_key: str, status: str, count: int, validated: bool) -> Dict[str, Any]:
        data = self.load()
        parts = data.get("parts", self._default_parts())
        parts[part_key] = {
            "status": status,
            "count": count,
            "validated": validated,
            "updated_at": datetime.now().isoformat(),
        }

        # Determine overall state transition
        new_state = self.get_state()
        if part_key == "part1" and status == "COMPLETE":
            new_state = PipelineState.PART_1_COMPLETE
        elif part_key == "part2a" and status == "COMPLETE":
            new_state = PipelineState.PART_2A_COMPLETE
        elif part_key == "part2b" and status == "COMPLETE":
            # Check if all core parts are complete
            p1_ok = parts.get("part1", {}).get("status") == "COMPLETE"
            p2a_ok = parts.get("part2a", {}).get("status") == "COMPLETE"
            if p1_ok and p2a_ok:
                new_state = PipelineState.CORE_COMPLETE
            else:
                new_state = PipelineState.PART_2B_COMPLETE
        elif part_key == "part3" and status == "COMPLETE":
            new_state = PipelineState.PART_3_COMPLETE

        return self.save(state=new_state, parts=parts)

    def is_part_complete(self, part_key: str) -> bool:
        data = self.load()
        p = data.get("parts", {}).get(part_key, {})
        return p.get("status") == "COMPLETE" and p.get("validated") is True

    def reset_checkpoint(self, state: PipelineState = PipelineState.BLUEPRINT_READY) -> Dict[str, Any]:
        """Resets the topic checkpoint to a specified state, clearing parts."""
        return self.save(state=state, parts=self._default_parts(), core_count=0, grand_test_count=0, notes="Reset")

