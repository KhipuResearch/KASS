---
title: Heterogeneous Treatment Effects
parent: Notebooks
nav_order: 1
---

# Heterogeneous Treatment Effects

When average treatment effects hide more than they reveal.

[View Interactive Demo →](../demos/Heterogeneous-Treatment-Effects.html){: .btn .btn-primary }
[View Source Notebook →](https://github.com/KhipuResearch/KASS/blob/main/notebooks/causal-inference/11-heterogeneous-treatment-effects.ipynb){: .btn }

---

## Overview

Average treatment effects can mask important variation. A job training program might help some workers dramatically while doing nothing for others. A policy might benefit urban areas while harming rural ones. This notebook demonstrates how to estimate treatment effect heterogeneity using modern machine learning methods.

---

## Methods

### Causal Forests

- Non-parametric estimation of conditional average treatment effects (CATEs)
- Automatic discovery of effect heterogeneity
- Valid confidence intervals via honest splitting

### Double Machine Learning

- Semi-parametric approach combining ML prediction with causal inference
- Robust to model misspecification
- Efficient estimation of average and heterogeneous effects

---

## When to Use This

**Good fit:**

- You have experimental or quasi-experimental data
- Effects likely vary by observable characteristics
- You need to target interventions efficiently
- Equity analysis requires understanding who benefits

**Not ideal:**

- Small sample sizes (needs 1,000+ observations)
- Treatment assignment depends on unobservables
- You only need average effects

---

## Key Assumptions

1. **Unconfoundedness**: Treatment assignment is as-good-as-random conditional on observables
2. **Overlap**: All subgroups have some treated and control units
3. **SUTVA**: No spillovers between units

---

## What You'll Learn

- How to implement causal forests using `econml`
- Visualizing treatment effect heterogeneity
- Policy targeting based on predicted effects
- Validation and robustness checks for CATE estimates
