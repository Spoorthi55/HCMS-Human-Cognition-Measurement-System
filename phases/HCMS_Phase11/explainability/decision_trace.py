def decision_trace(profile):
    trace = []

    if profile["accuracy"] < 0.7:
        trace.append("Low accuracy detected")
    if profile["confidence"] > profile["accuracy"]:
        trace.append("Overconfidence identified")
    if profile["consistency"] < 0.75:
        trace.append("Response instability detected")

    return trace

if __name__ == "__main__":
    sample_profile = {
        "accuracy": 0.6,
        "confidence": 0.8,
        "consistency": 0.67
    }

    trace = decision_trace(sample_profile)
    print("Decision Trace:")
    for t in trace:
        print("-", t)
