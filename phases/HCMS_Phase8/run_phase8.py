import json
from adaptation.feedback_engine import generate_feedback
from strategies.remediation import remediation_strategy
from strategies.reinforcement import reinforcement_strategy

# Load Phase 7 output
with open("../HCMS_Phase7/outputs/cognitive_summary.json") as f:
    cognitive_summary = json.load(f)

feedback = generate_feedback(
    cognitive_summary,
    "adaptation/intervention_rules.json"
)

adaptive_plan = {
    "feedback": feedback,
    "remediation": remediation_strategy(),
    "reinforcement": reinforcement_strategy()
}

with open("outputs/adaptive_feedback.json", "w") as f:
    json.dump(adaptive_plan, f, indent=4)

print("=== ADAPTIVE FEEDBACK GENERATED ===")
print(json.dumps(adaptive_plan, indent=2))
