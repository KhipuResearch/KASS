---
title: Notebooks
nav_order: 3
has_children: true
---

# Notebooks

Each notebook solves a specific analytical problem using methods appropriate to the data structure and identification challenge.

---

## Causal Inference Methods

Methods for estimating causal effects when randomization isn't possible:

| Notebook | Use When | Key Technique |
|----------|----------|---------------|
| [Heterogeneous Treatment Effects](heterogeneous-treatment-effects) | Effects vary across subgroups | Causal Forests, Double ML |
| [Synthetic Control](synthetic-control) | Single treated unit, no parallel trends | Weighted donor pools |
| [Regression Discontinuity](regression-discontinuity) | Policy threshold exists | Local polynomial regression |

---

## Applied Policy Analysis

Production-ready templates for common policy questions:

| Notebook | Policy Domain | Data Sources |
|----------|---------------|--------------|
| [Labor Market Intelligence](labor-market-intelligence) | Workforce development | BLS, Census, QCEW |
| [Opportunity Zone Evaluation](opportunity-zone-evaluation) | Place-based programs | Census, IRS, HMDA |
| [Workforce Development ROI](workforce-development-roi) | Program evaluation | Administrative earnings |

---

## Choosing the Right Method

### You have a policy threshold (eligibility cutoff, score, date)

→ Use [Regression Discontinuity](regression-discontinuity)

### You're evaluating one treated unit (state, city, organization)

→ Use [Synthetic Control](synthetic-control)

### You need to know who benefits most from an intervention

→ Use [Heterogeneous Treatment Effects](heterogeneous-treatment-effects)

### You're analyzing local labor markets

→ Use [Labor Market Intelligence](labor-market-intelligence)

### You're evaluating a federal place-based program

→ Use [Opportunity Zone Evaluation](opportunity-zone-evaluation)

### You need OMB-compliant cost-benefit analysis

→ Use [Workforce Development ROI](workforce-development-roi)
