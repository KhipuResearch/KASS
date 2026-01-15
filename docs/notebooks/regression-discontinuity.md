---
title: Regression Discontinuity
parent: Notebooks
nav_order: 3
---

# Regression Discontinuity Toolkit

Exploits policy thresholds to identify causal effects.

[View Interactive Demo →](../demos/Regression-Discontinuity-Toolkit.html){: .btn .btn-primary }
[View Source Notebook →](https://github.com/KhipuResearch/KASS/blob/main/notebooks/causal-inference/15-regression-discontinuity-toolkit.ipynb){: .btn }

---

## Overview

Many policies create sharp thresholds: test scores determine program eligibility, income cutoffs determine benefits, geographic boundaries determine treatment. Regression discontinuity exploits these thresholds to estimate causal effects by comparing units just above and just below the cutoff.

---

## Methods

### Sharp RD

- Units above threshold receive treatment, below don't
- Local polynomial regression at the cutoff
- Optimal bandwidth selection (MSE-optimal, coverage-optimal)

### Fuzzy RD

- Threshold affects treatment probability, not certainty
- Instrumental variables approach
- Estimates local average treatment effect (LATE)

### Specification Tests

- Manipulation testing (density discontinuity)
- Covariate balance at threshold
- Placebo cutoffs and sensitivity analysis

---

## When to Use This

**Good fit:**

- Clear policy threshold based on running variable
- Units can't precisely manipulate their position
- Sufficient observations near the threshold
- You want local causal effects at the cutoff

**Not ideal:**

- Threshold is manipulable
- Sparse data near cutoff
- Need effects far from threshold
- Multiple overlapping thresholds

---

## Key Assumptions

1. **No manipulation**: Units can't precisely sort around the threshold
2. **Continuity**: Potential outcomes are continuous at the cutoff
3. **Local effect**: Estimates apply to units at the threshold

---

## What You'll Learn

- Sharp and fuzzy RD implementation
- Bandwidth selection algorithms
- Manipulation testing (McCrary density test)
- Visualization best practices for RD
