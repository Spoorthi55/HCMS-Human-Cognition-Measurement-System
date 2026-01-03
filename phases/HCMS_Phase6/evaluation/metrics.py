def evaluate_system(consistency_scores, confidence_corr):
    avg_consistency = consistency_scores.mean()

    print("\n=== SYSTEM METRICS ===")
    print(f"Average Consistency: {round(avg_consistency, 2)}")
    print(f"Confidence-Accuracy Correlation: {round(confidence_corr, 2)}")

    return {
        "avg_consistency": avg_consistency,
        "confidence_accuracy_corr": confidence_corr
    }
