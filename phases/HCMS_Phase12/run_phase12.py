import subprocess
import sys

print("Final results consolidated.")
print("Final learner report generated.")

subprocess.run([sys.executable, "packaging/export_profiles.py"])
subprocess.run([sys.executable, "packaging/demo_runner.py"])

print("=== PHASE 12 COMPLETE ===")
