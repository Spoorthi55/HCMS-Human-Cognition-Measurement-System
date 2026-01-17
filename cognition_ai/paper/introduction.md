# Introduction

Correct answers are commonly treated as evidence of understanding. In educational assessment, automated grading systems, and standardized testing, performance is typically summarized as a static accuracy score. While efficient, this paradigm implicitly assumes that correctness reflects stable mastery. In practice, however, correct responses can arise from guessing, short-term memorization, pattern matching, or brittle reasoning strategies that do not generalize beyond the immediate context.

This limitation has long been acknowledged in learning science and cognitive psychology. Research on metacognition emphasizes that understanding is not only a function of what a learner answers, but also how confident they are, how consistently they reason across trials, and how their performance responds to variation or uncertainty. Despite this, most computational assessment systems continue to equate correctness with comprehension, offering limited insight into the robustness of a learner’s knowledge.

As a result, two learners with identical test scores may possess fundamentally different cognitive states. One may exhibit stable, well-calibrated understanding, while another may display overconfidence, inconsistency, or fragile reasoning that degrades under minimal perturbation. Accuracy-based evaluation is unable to distinguish between these cases, raising a critical question: **Are static test scores reliable indicators of true understanding?**

This paper investigates this question by treating cognition as a multi-dimensional construct rather than a single outcome variable. We introduce the **Human Cognition Measurement System (HCMS)**, a cognition-aware assessment framework designed to probe understanding beyond correctness. HCMS integrates multiple behavioral signals—accuracy, self-reported confidence, repeated-trial consistency, and stability under controlled perturbation—to infer cognitive robustness and metacognitive alignment.

Importantly, HCMS is not proposed as a replacement for existing assessment models, but as a complementary measurement instrument. Its purpose is to reveal cognitive properties that correctness-based metrics systematically obscure, particularly in cases where surface performance appears strong.

Through controlled experiments, we demonstrate that learners with similar accuracy profiles often diverge substantially in confidence calibration and reasoning stability. These divergences become pronounced under perturbation, where miscalibrated learners exhibit significant degradation in cognitive consistency despite unchanged accuracy. These findings suggest that correctness alone is an incomplete and potentially misleading proxy for understanding.

The contributions of this work are threefold:
- We formalize cognition-aware assessment as the measurement of stability and calibration, not only correctness.
- We present HCMS as an interpretable framework for operationalizing these latent cognitive dimensions.
- We provide empirical evidence that confidence–accuracy misalignment predicts instability that static test scores fail to capture.

By reframing assessment as cognitive measurement rather than answer verification, this work aims to advance the design of systems that measure **how people understand**, not merely **what they answer**.
