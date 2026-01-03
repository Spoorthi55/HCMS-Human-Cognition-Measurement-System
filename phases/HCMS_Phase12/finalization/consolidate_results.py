import json

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

final_results = {
    "learner_profile": load_json("../HCMS_Phase5/outputs/learner_profile.json"),
    "system_metrics": {
        "consistency": 0.83,
        "confidence_accuracy_corr": 0.23
    },
    "insights": [
        "Partial Understanding",
        "Overconfidence detected",
        "Response instability observed"
    ],
    "adaptation": load_json("../HCMS_Phase8/outputs/adaptive_feedback.json"),
    "robustness": {
        "confidence_stability_std": 0.632
    }
}

with open("final_results.json", "w") as f:
    json.dump(final_results, f, indent=4)

print("Final results consolidated.")
