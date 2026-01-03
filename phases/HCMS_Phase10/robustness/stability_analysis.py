import pandas as pd
import numpy as np
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "responses.csv"

df = pd.read_csv(DATA_PATH, header=0)

CONF_COL = df.columns[6]

std_dev = np.std(df[CONF_COL].astype(float))

print(f"Confidence Stability (Std Dev): {std_dev:.3f}")
