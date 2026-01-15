---
title: Regression Discontinuity
parent: Notebooks
nav_order: 3
---

# Regression Discontinuity Toolkit

Exploits policy thresholds to identify causal effects.

<div class="demo-links">
  <a href="../demos/Regression-Discontinuity-Toolkit.html" class="btn btn-primary">View Interactive Demo</a>
  <a href="https://github.com/KhipuResearch/KASS/blob/main/notebooks/causal-inference/15-regression-discontinuity-toolkit.ipynb" class="btn btn-outline">View Source</a>
</div>

---

## Overview

Many policies create sharp thresholds: test scores determine program eligibility, income cutoffs determine benefits. Regression discontinuity exploits these thresholds to estimate causal effects by comparing units just above and just below the cutoff.

---

## Methods

### Sharp RD
- Units above threshold receive treatment, below don't
- Local polynomial regression at the cutoff
- Optimal bandwidth selection

### Fuzzy RD
- Threshold affects treatment probability, not certainty
- Instrumental variables approach
- Estimates local average treatment effect (LATE)

### Specification Tests
- Manipulation testing (density discontinuity)
- Covariate balance at threshold
- Placebo cutoffs

---

## When to Use This

**Good fit:**
- Clear policy threshold based on running variable
- Units can't precisely manipulate their position
- Sufficient observations near the threshold

**Not ideal:**
- Threshold is manipulable
- Sparse data near cutoff
- Need effects far from threshold

---

## Key Assumptions

1. **No manipulation**: Units can't precisely sort around the threshold
2. **Continuity**: Potential outcomes are continuous at the cutoff
3. **Local effect**: Estimates apply to units at the threshold
