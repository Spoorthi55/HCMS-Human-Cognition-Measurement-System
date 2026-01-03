from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parents[1]
report_path = BASE_DIR / "release" / "final_learner_report.json"

if not report_path.exists():
    raise FileNotFoundError("Final learner report not found in release folder.")

with open(report_path) as f:
    report = json.load(f)

print("=== DEMO OUTPUT ===")
for k, v in report.items():
    print(f"{k}: {v}")
