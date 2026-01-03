import json

with open("final_results.json") as f:
    data = json.load(f)

summary = {
    "Understanding Level": "Partial",
    "Calibration": "Miscalibrated",
    "Consistency Score": data["system_metrics"]["consistency"],
    "System Verdict": "Needs targeted remediation"
}

with open("final_learner_report.json", "w") as f:
    json.dump(summary, f, indent=4)

print("Final learner report generated.")
