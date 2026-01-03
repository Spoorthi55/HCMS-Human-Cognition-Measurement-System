import pandas as pd
import numpy as np
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "responses.csv"

df = pd.read_csv(DATA_PATH, header=0)

# Confidence is column index 6
CONF_COL = df.columns[6]

df["noisy_confidence"] = df[CONF_COL].astype(float) + np.random.normal(0, 0.1, len(df))

print("Noisy confidence generated successfully.")
print(df[[CONF_COL, "noisy_confidence"]].head())
