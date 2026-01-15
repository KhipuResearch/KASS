---
title: Home
layout: home
nav_order: 1
---

# KASS: Knowledge & Analytics for Social Science

Production-grade causal inference notebooks for policy analysis.

---

## What This Is

KASS is a curated set of Jupyter notebooks that tackle real policy questions using rigorous causal inference methods. These aren't toy examples—they're the kind of analyses that federal agencies, research institutions, and policy shops actually run.

- **A showcase** of what's possible with modern econometric methods
- **A learning resource** for applied researchers who need to estimate causal effects
- **A technical proof-of-concept** for the [KRL (Khipu Research Labs)](https://krlabs.dev) platform

---

## Interactive Demos

View the fully rendered notebooks with all outputs, visualizations, and results:

| Notebook | Method | View |
|----------|--------|------|
| Heterogeneous Treatment Effects | Causal Forests, Double ML | [View Demo →](demos/Heterogeneous-Treatment-Effects.html) |
| Synthetic Control Policy Lab | Synthetic Control Method | [View Demo →](demos/Synthetic-Control-Policy-Lab.html) |
| Regression Discontinuity Toolkit | RDD, Bandwidth Selection | [View Demo →](demos/Regression-Discontinuity-Toolkit.html) |
| Labor Market Intelligence | BLS/Census Integration | [View Demo →](demos/Labor-Market-Intelligence.html) |
| Opportunity Zone Evaluation | DiD, Synthetic Controls | [View Demo →](demos/Opportunity-Zone-Evaluation.html) |
| Workforce Development ROI | Cost-Benefit Analysis | [View Demo →](demos/Workforce-Development-ROI.html) |

---

## Why This Exists

Policy analysis has a credibility problem. Too much of what passes for "evaluation" relies on correlations dressed up as causation. Too many decisions get made on gut feeling because rigorous analysis takes too long.

We built KASS to demonstrate what changes when you have:

- **Proper causal inference methodologies** baked into your workflow
- **Direct access to authoritative data sources** (Census, BLS, administrative records)
- **Reproducible pipelines** that anyone can audit and extend

---

## Quick Start

```bash
git clone https://github.com/KhipuResearch/KASS.git
cd KASS
pip install -r requirements.txt
jupyter lab
```

<div class="demo-links">
  <a href="getting-started" class="btn btn-primary">Get Started</a>
  <a href="https://github.com/KhipuResearch/KASS" class="btn btn-outline">View on GitHub</a>
</div>
