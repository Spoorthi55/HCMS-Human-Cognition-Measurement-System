import json

def generate_feedback(cognitive_summary, rules_path):
    with open(rules_path) as f:
        rules = json.load(f)

    feedback = []

    calibration = cognitive_summary.get("Calibration") or cognitive_summary.get("Calibration Status")
    consistency = cognitive_summary.get("Consistency", 1.0)

    if calibration == "Miscalibrated":
        feedback.append(rules["miscalibrated"])

    if consistency < 0.8:
        feedback.append(rules["low_consistency"])

    return feedback
