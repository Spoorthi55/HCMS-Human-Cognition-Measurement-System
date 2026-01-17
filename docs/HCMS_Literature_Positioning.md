# Literature Positioning — HCMS

## Research Context

This work lies at the intersection of:
- Cognitive assessment
- Metacognition and confidence calibration
- Learning stability and robustness
- Human-centered measurement in AI systems

While substantial research has examined correctness, confidence, and uncertainty in isolation, most computational assessment systems continue to rely on **static performance metrics** as proxies for understanding. This creates a gap between what is measured and how human cognition actually behaves under uncertainty, repetition, and variation.

HCMS is positioned as a **cognition measurement framework**, not a performance predictor, designed to probe this gap.

---

## 1. Performance-Centric Assessment Models

**Representative Work:** Classical Test Theory, Item Response Theory (IRT)

**What they measure:**  
- Response correctness  
- Item difficulty  
- Latent ability estimates  

**Core assumption:**  
Aggregated correctness reliably reflects underlying understanding.

**What they do not capture:**  
These models do not measure confidence calibration, reasoning consistency, or stability under perturbation. Learners with identical scores are treated as cognitively equivalent despite potentially large differences in certainty, robustness, and conceptual grounding.

**HCMS distinction:**  
HCMS explicitly decouples correctness from cognitive robustness, allowing equivalent performance outcomes to yield distinct cognitive profiles.

---

## 2. Confidence Calibration and Metacognition Research

**Representative Work:** Confidence–accuracy calibration studies in cognitive psychology and education

**What they measure:**  
- Self-reported confidence  
- Calibration error and bias  
- Overconfidence and underconfidence patterns  

**Core assumption:**  
Confidence is an informative but auxiliary signal.

**What they do not capture:**  
Most studies analyze confidence independently, without integrating consistency, longitudinal behavior, or robustness into a unified measurement model.

**HCMS distinction:**  
HCMS treats confidence–accuracy alignment as a **structural cognitive signal**, jointly analyzed with stability and consistency rather than as a post-hoc diagnostic.

---

## 3. Intelligent Tutoring and Learner Modeling Systems

**Representative Work:** Knowledge tracing, adaptive tutoring frameworks

**What they measure:**  
- Probability of correctness  
- Learning progression over time  

**Core assumption:**  
Improved performance implies improved understanding.

**What they do not capture:**  
These systems focus on adaptation and prediction but rarely diagnose *why* performance is stable or fragile, particularly when accuracy masks miscalibration or brittle reasoning.

**HCMS distinction:**  
HCMS prioritizes cognitive diagnosis over adaptation, identifying latent instability even when surface-level performance appears strong.

---

## 4. Explainable AI in Educational Contexts

**Representative Work:** Explainable learner analytics and assessment models

**What they measure:**  
- Feature importance  
- Model transparency  

**Core assumption:**  
Explainability improves trust in predictions.

**What they do not capture:**  
Explainability is typically applied to outcome prediction, not to the formation and stability of cognitive states themselves.

**HCMS distinction:**  
HCMS applies interpretability at the level of cognitive measurement, enabling traceable reasoning about how cognitive states are inferred.

---

## 5. Positioning Summary

Existing approaches tend to:
- Measure performance without diagnosing cognition  
- Analyze confidence without integration  
- Adapt instruction without measuring robustness  

**HCMS occupies a complementary position** by framing assessment as a problem of **cognitive validity**, explicitly measuring confidence–accuracy alignment and stability under perturbation.

HCMS does not replace existing assessment paradigms; rather, it introduces a measurement layer that captures cognitive properties systematically obscured by static correctness-based evaluation.
