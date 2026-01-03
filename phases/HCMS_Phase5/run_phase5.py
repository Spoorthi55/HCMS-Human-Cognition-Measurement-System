from inference.cognitive_inference import infer_cognition
import json

# Example from Phase 4 output
learner_data = [
    {"concept": "Conditionals", "accuracy": 0.4, "attempts": 2, "confidence": 0.5},
    {"concept": "Variables", "accuracy": 0.2, "attempts": 1, "confidence": 0.6}
]

profiles = []

for data in learner_data:
    profile = infer_cognition(
        data["concept"],
        data["accuracy"],
        data["attempts"],
        data["confidence"]
    )
    profiles.append(profile)

with open("outputs/learner_profile.json", "w") as f:
    json.dump(profiles, f, indent=4)

print("✅ Learner cognitive profile generated.")
