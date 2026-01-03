import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

src = BASE_DIR / "finalization" / "final_learner_report.json"
dst = BASE_DIR / "release" / "final_learner_report.json"

if not src.exists():
    raise FileNotFoundError(f"Source file not found: {src}")

dst.parent.mkdir(exist_ok=True)
shutil.copy(src, dst)

print("Final learner report exported to release folder.")
