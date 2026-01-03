import json
import os

os.makedirs("outputs", exist_ok=True)

cognitive_summary = {
    "understanding_level": "Partial Understanding",
    "calibration": "Miscalibrated",
    "consistency": 0.67,
    "insights": [
        "Learner is overconfident",
        "Learner responses are unstable"
    ]
}

with open("outputs/cognitive_summary.json", "w") as f:
    json.dump(cognitive_summary, f, indent=4)

print("Cognitive summary saved successfully.")
