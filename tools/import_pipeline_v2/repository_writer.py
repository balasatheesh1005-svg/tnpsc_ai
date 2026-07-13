"""Write a new JSON repository file; never modify existing files."""
import json
from pathlib import Path


def write(questions, output_path):
    path = Path(output_path)
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite existing repository: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(list(questions or []), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"output_file": str(path), "written_count": len(questions or [])}
