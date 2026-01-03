from validation.consistency_checks import check_consistency
from validation.confidence_vs_accuracy import confidence_accuracy_relation
from evaluation.metrics import evaluate_system

csv_path = "experiments/repeated_trials.csv"

consistency = check_consistency(csv_path)
confidence_corr = confidence_accuracy_relation(csv_path)

evaluate_system(consistency, confidence_corr)
