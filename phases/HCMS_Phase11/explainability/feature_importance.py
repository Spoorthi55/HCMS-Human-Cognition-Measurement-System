import json

FEATURE_WEIGHTS = {
    "accuracy": 0.4,
    "confidence": 0.3,
    "consistency": 0.2,
    "attempts": 0.1
}

def compute_feature_importance():
    total = sum(FEATURE_WEIGHTS.values())
    importance = {k: v / total for k, v in FEATURE_WEIGHTS.items()}
    return importance

if __name__ == "__main__":
    importance = compute_feature_importance()
    with open("outputs/feature_importance.json", "w") as f:
        json.dump(importance, f, indent=2)
    print("Feature importance computed.")
