import streamlit as st
import sqlite3
from datetime import datetime
from questions import QUESTIONS

# =============================
# DATABASE
# =============================
conn = sqlite3.connect("cognition.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    concept TEXT,
    question_id TEXT,
    correct INTEGER,
    confidence INTEGER,
    explanation TEXT,
    timestamp TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS cognitive_state (
    user TEXT,
    concept TEXT,
    mastery REAL,
    calibration_error REAL,
    attempts INTEGER,
    PRIMARY KEY (user, concept)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS misconceptions (
    user TEXT,
    concept TEXT,
    misconception TEXT,
    count INTEGER,
    PRIMARY KEY (user, concept, misconception)
)
""")

conn.commit()

# =============================
# STATE FUNCTIONS
# =============================
def get_state(user, concept):
    c.execute(
        "SELECT mastery, calibration_error, attempts FROM cognitive_state WHERE user=? AND concept=?",
        (user, concept)
    )
    row = c.fetchone()
    return row if row else (0.5, 0.0, 0)

def update_state(user, concept, correct, confidence):
    mastery, cal_err, attempts = get_state(user, concept)
    attempts += 1

    confidence_norm = confidence / 5
    error = (confidence_norm - correct) ** 2

    mastery = mastery + 0.15 * (correct - mastery)
    cal_err = ((cal_err * (attempts - 1)) + error) / attempts

    c.execute("""
    INSERT OR REPLACE INTO cognitive_state
    VALUES (?, ?, ?, ?, ?)
    """, (user, concept, mastery, cal_err, attempts))
    conn.commit()

def log_misconception(user, concept, explanation, question):
    text = explanation.lower()
    for m in question["misconceptions"]:
        if m in text:
            c.execute("""
            INSERT INTO misconceptions VALUES (?, ?, ?, 1)
            ON CONFLICT(user, concept, misconception)
            DO UPDATE SET count = count + 1
            """, (user, concept, m))
            conn.commit()

# =============================
# QUESTION CONTROL
# =============================
def unanswered_questions(user, concept):
    c.execute("""
    SELECT question_id FROM responses
    WHERE user=? AND concept=?
    """, (user, concept))
    answered = {r[0] for r in c.fetchall()}
    return [q for q in QUESTIONS if q["concept"] == concept and q["id"] not in answered]

# =============================
# SESSION STATE
# =============================
if "question" not in st.session_state:
    st.session_state.question = None

# =============================
# UI
# =============================
st.title("Human Cognition Measurement System (HCMS)")
st.caption("Research Instrument — Measuring Understanding")

user = st.text_input("Enter your username")
concepts = sorted(set(q["concept"] for q in QUESTIONS))
concept = st.selectbox("Select Concept", concepts)

if user and concept:
    pool = unanswered_questions(user, concept)
    if not pool:
        st.info("All questions for this concept completed.")
    else:
        if st.session_state.question is None:
            st.session_state.question = pool[0]

        q = st.session_state.question
        st.code(q["question"])

        ans = st.text_input("What will be printed?")
        exp = st.text_area("Explain your reasoning")
        conf = st.slider("How confident are you?", 1, 5, 3)

        if st.button("Submit"):
            correct = int(ans.strip() == q["answer"])

            c.execute("""
            INSERT INTO responses VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)
            """, (user, concept, q["id"], correct, conf, exp, datetime.now().isoformat()))

            update_state(user, concept, correct, conf)
            if not correct:
                log_misconception(user, concept, exp, q)

            st.session_state.question = None
            st.success("Correct ✅" if correct else "Incorrect ❌")

    mastery, cal_err, attempts = get_state(user, concept)

    st.subheader("Cognitive Profile")
    st.write(f"Mastery: {round(mastery, 2)}")
    st.write(f"Confidence Calibration Error: {round(cal_err, 3)}")
    st.write(f"Attempts: {attempts}")

    c.execute("SELECT misconception, count FROM misconceptions WHERE user=? AND concept=?", (user, concept))
    rows = c.fetchall()
    st.subheader("Detected Misconceptions")
    st.write(rows if rows else "None detected.")
