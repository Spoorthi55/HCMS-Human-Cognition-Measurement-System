import json
from models.mastery_model import compute_mastery
from models.confidence_model import confidence_alignment

def infer_cognition(concept, accuracy, attempts, confidence):
    mastery = compute_mastery(accuracy, attempts)
    confidence_score = confidence_alignment(confidence, accuracy)

    return {
        "concept": concept,
        "mastery": mastery,
        "confidence_alignment": confidence_score
    }
