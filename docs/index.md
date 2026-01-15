---
title: Home
layout: home
nav_order: 1
---

# KASS – KHIPU Analytics for Social Science

**Open-source notebooks demonstrating production-grade causal inference and policy analysis**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## What This Is

KASS is a curated set of Jupyter notebooks that tackle real policy questions using rigorous causal inference methods. These aren't toy examples. They're the kind of analyses that federal agencies, research institutions, and policy shops actually run—complete with proper identification strategies, robustness checks, and transparent limitations.

Think of this repository as:

- **A showcase** of what's possible with modern econometric methods
- **A learning resource** for applied researchers who need to estimate causal effects
- **A technical proof-of-concept** for the [KRL (Khipu Research Labs)](https://krlabs.dev) platform

If you've ever struggled with messy policy data, debated whether your treatment effects are believable, or wondered whether your regression discontinuity design would survive peer review, you're in the right place.

---

## Why This Exists

Policy analysis has a credibility problem. Too much of what passes for "evaluation" relies on correlations dressed up as causation. Too many decisions get made on gut feeling because rigorous analysis takes too long. And too many researchers waste time rebuilding analytical infrastructure that should be standardized by now.

We built KASS to demonstrate what changes when you have:

- **Proper causal inference methodologies** baked into your workflow
- **Direct access to authoritative data sources** (Census, BLS, administrative records)
- **Reproducible pipelines** that anyone can audit and extend

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

## Quick Links

- [Getting Started](getting-started) – Installation and usage guide
- [Notebooks](notebooks/) – Detailed method documentation
- [Methodology](methodology) – Quality standards and approach
- [Contributing](contributing) – How to contribute
