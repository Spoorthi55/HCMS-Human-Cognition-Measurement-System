def summarize_cognition(profile):
    mastery = profile["mastery"]
    confidence = profile["confidence"]
    consistency = profile["consistency"]

    if mastery > 0.75:
        level = "Strong Understanding"
    elif mastery > 0.4:
        level = "Partial Understanding"
    else:
        level = "Weak Understanding"

    calibration = "Well-calibrated" if abs(confidence - mastery) < 0.2 else "Miscalibrated"

    return {
        "Understanding Level": level,
        "Calibration": calibration,
        "Consistency": round(consistency, 2)
    }
