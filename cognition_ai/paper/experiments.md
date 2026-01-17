# Experiments

The experimental design aims to evaluate whether correctness-based performance sufficiently reflects stable understanding, and whether additional cognitive signals—particularly confidence calibration and consistency—provide meaningful explanatory power beyond accuracy alone.

All experiments were conducted using structured learner response data collected across multiple concept-level tasks. Each learner interaction included a response label, a self-reported confidence score, and a temporal identifier, enabling repeated-trial and stability analysis.

## Experimental Objectives

The experiments were designed to answer three core questions:

1. Can learners with similar accuracy exhibit different cognitive stability profiles?
2. Does confidence–accuracy misalignment correlate with degradation under perturbation?
3. Can cognition-aware metrics distinguish robust understanding from brittle correctness?

## Experimental Setup

Learners completed multiple trials on semantically consistent tasks targeting the same underlying concept. For each trial, learners provided:
- A binary or categorical response
- A normalized confidence rating
- A timestamped interaction record

HCMS processed these inputs through its cognitive inference pipeline, producing per-learner metrics for accuracy, confidence calibration, and consistency.

To isolate cognitive stability, no adaptive feedback was provided during experimental trials.

## Cognitive Profiling and Grouping

Learners were grouped based on confidence–accuracy alignment, computed as the correlation between confidence ratings and response correctness across trials.

Two primary cognitive profiles emerged:
- **Calibrated learners** — high alignment between confidence and correctness
- **Miscalibrated learners** — systematic overconfidence or underconfidence

Importantly, grouping was performed independently of raw accuracy, allowing comparison between learners with comparable performance scores.

## Controlled Perturbation Protocol

To test robustness, learners were exposed to controlled perturbations applied to previously encountered tasks. Perturbations were designed to preserve semantic meaning while introducing minimal variation, such as:
- Rephrased prompts
- Altered surface structure
- Injected response noise

Perturbations were applied uniformly across learner groups.

## Stability Metrics

Cognitive stability was measured using:
- Change in consistency scores across trials
- Variance in confidence ratings
- Deviation in inferred cognitive state

Stability degradation was quantified as the difference between baseline and perturbed conditions.

## Evaluation Criteria

The primary evaluation focused on divergence between accuracy-based and cognition-based assessment outcomes. Specifically, we examined cases where accuracy remained stable but cognitive stability deteriorated under perturbation.

This design enables direct evaluation of whether static test scores mask meaningful differences in underlying understanding.

## Reproducibility

All experimental procedures, metrics, and configurations are deterministic and fully reproducible. Experimental artifacts, including configuration files and summary statistics, are generated automatically by the HCMS pipeline and preserved for independent verification.
