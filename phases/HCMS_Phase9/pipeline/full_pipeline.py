import json
import subprocess

def run_phase(cmd, label):
    print(f"\n=== Running {label} ===")
    subprocess.run(cmd, shell=True)

def main():
    run_phase("python ../HCMS_Phase4/analysis.py", "Phase 4: Analysis")
    run_phase("python ../HCMS_Phase5/run_phase5.py", "Phase 5: Modeling")
    run_phase("python ../HCMS_Phase6/run_phase6.py", "Phase 6: Validation")
    run_phase("python ../HCMS_Phase7/run_phase7.py", "Phase 7: Interpretation")
    run_phase("python ../HCMS_Phase8/run_phase8.py", "Phase 8: Adaptation")

    print("\n✅ HCMS FULL PIPELINE COMPLETE")

if __name__ == "__main__":
    main()
