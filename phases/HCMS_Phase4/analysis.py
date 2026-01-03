import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# LOAD DATA
# =========================
conn = sqlite3.connect("data/cognition.db")

responses = pd.read_sql("SELECT * FROM responses", conn)
state = pd.read_sql("SELECT * FROM cognitive_state", conn)
misconceptions = pd.read_sql("SELECT * FROM misconceptions", conn)

print("=== DATA LOADED ===")
print(f"Responses: {len(responses)} rows")
print(f"Cognitive State: {len(state)} rows")
print(f"Misconceptions: {len(misconceptions)} rows")

# =========================
# RESPONSE ACCURACY BY CONCEPT
# =========================
accuracy = (
    responses
    .groupby("concept")["correct"]
    .mean()
    .reset_index()
)

# =========================
# PLOT 1 — ACCURACY
# =========================
plt.figure()
plt.bar(accuracy["concept"], accuracy["correct"])
plt.ylim(0, 1)
plt.title("Accuracy by Concept")
plt.ylabel("Accuracy")
plt.xlabel("Concept")
plt.show()

# =========================
# PLOT 2 — MASTERY VS CONFIDENCE ERROR
# =========================
plt.figure()
plt.scatter(state["mastery"], state["calibration_error"])
plt.xlabel("Mastery")
plt.ylabel("Confidence Calibration Error")
plt.title("Mastery vs Confidence Calibration")
plt.show()

# =========================
# PLOT 3 — ATTEMPTS VS MASTERY
# =========================
plt.figure()
plt.scatter(state["attempts"], state["mastery"])
plt.xlabel("Attempts")
plt.ylabel("Mastery")
plt.title("Practice vs Mastery")
plt.show()
