import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "responses.csv"

df = pd.read_csv(DATA_PATH, header=0)

CONF_COL = df.columns[6]

df["adversarial_confidence"] = 5 - df[CONF_COL].astype(float)

print("Adversarial confidence generated successfully.")
print(df[[CONF_COL, "adversarial_confidence"]].head())
