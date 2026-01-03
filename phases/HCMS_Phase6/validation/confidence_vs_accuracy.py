import pandas as pd

def confidence_accuracy_relation(csv_path):
    df = pd.read_csv(csv_path)

    correlation = df["accuracy"].corr(df["confidence"])

    print("\n=== CONFIDENCE vs ACCURACY ===")
    print(f"Correlation: {round(correlation, 2)}")

    if correlation > 0.5:
        print("Good calibration ✅")
    else:
        print("Poor calibration ⚠️")

    return correlation
