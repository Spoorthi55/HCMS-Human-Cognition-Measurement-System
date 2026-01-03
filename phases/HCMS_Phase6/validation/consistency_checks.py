import pandas as pd

def check_consistency(csv_path):
    df = pd.read_csv(csv_path)

    consistency = df.groupby("user_id")["accuracy"].mean()

    print("\n=== CONSISTENCY CHECK ===")
    for user, score in consistency.items():
        print(f"{user}: Consistency Score = {round(score, 2)}")

    return consistency
