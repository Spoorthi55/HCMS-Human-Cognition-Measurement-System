import os

print("=== PHASE 10: ROBUSTNESS TESTING ===")

os.system("python stress_tests/noisy_inputs.py")
os.system("python stress_tests/adversarial_cases.py")
os.system("python robustness/stability_analysis.py")

print("=== PHASE 10 COMPLETE ===")
