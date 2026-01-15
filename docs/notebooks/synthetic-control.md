---
title: Synthetic Control
parent: Notebooks
nav_order: 2
---

# Synthetic Control Policy Lab

For situations where randomization is impossible and parallel trends are questionable.

[View Interactive Demo →](../demos/Synthetic-Control-Policy-Lab.html){: .btn .btn-primary }
[View Source Notebook →](https://github.com/KhipuResearch/KASS/blob/main/notebooks/causal-inference/14-synthetic-control-policy-lab.ipynb){: .btn }

---

## Overview

When evaluating policies that affect entire units (states, countries, organizations), traditional methods often fail. Difference-in-differences requires parallel trends. Matching requires many similar units. Synthetic control constructs a counterfactual from weighted combinations of donor units, providing rigorous causal inference even with a single treated unit.

---

## Methods

### Classic Synthetic Control

- Optimal weighting of control units to match pre-treatment outcomes
- No functional form assumptions
- Transparent weights reveal comparison strategy

### Uncertainty Quantification

- Placebo tests using untreated units
- Permutation inference for p-values
- Confidence intervals via conformal inference

---

## When to Use This

**Good fit:**

- Single treated unit (or few treated units)
- Good pre-treatment outcome data
- Pool of plausible comparison units
- Treatment timing is sharp

**Not ideal:**

- Treatment affects all potential donors (spillovers)
- Short pre-treatment period
- Outcome is highly volatile
- Multiple staggered treatments

---

## Key Assumptions

1. **No anticipation**: Units don't change behavior before treatment
2. **No spillovers**: Treatment doesn't affect control units
3. **Convex hull**: Treated unit is within the range of controls
4. **Stable relationships**: Pre-treatment fit predicts post-treatment fit

---

## What You'll Learn

- Implementing synthetic control from scratch
- Weight interpretation and donor selection
- Placebo testing and inference
- When synthetic control fails and alternatives
