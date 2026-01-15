---
layout: page
title: Notebooks
permalink: /notebooks/
---

Each notebook solves a specific analytical problem using methods appropriate to the data structure and identification challenge.

---

## Causal Inference Methods

Methods for estimating causal effects when randomization isn't possible:

| Notebook | Use When | Key Technique |
|----------|----------|---------------|
| [Heterogeneous Treatment Effects]({{ site.baseurl }}/demos/Heterogeneous-Treatment-Effects.html) | Effects vary across subgroups | Causal Forests, Double ML |
| [Synthetic Control]({{ site.baseurl }}/demos/Synthetic-Control-Policy-Lab.html) | Single treated unit, no parallel trends | Weighted donor pools |
| [Regression Discontinuity]({{ site.baseurl }}/demos/Regression-Discontinuity-Toolkit.html) | Policy threshold exists | Local polynomial regression |

---

## Applied Policy Analysis

Production-ready templates for common policy questions:

| Notebook | Policy Domain | Data Sources |
|----------|---------------|--------------|
| [Labor Market Intelligence]({{ site.baseurl }}/demos/Labor-Market-Intelligence.html) | Workforce development | BLS, Census, QCEW |
| [Opportunity Zone Evaluation]({{ site.baseurl }}/demos/Opportunity-Zone-Evaluation.html) | Place-based programs | Census, IRS, HMDA |
| [Workforce Development ROI]({{ site.baseurl }}/demos/Workforce-Development-ROI.html) | Program evaluation | Administrative earnings |

---

## Choosing the Right Method

### You have a policy threshold (eligibility cutoff, score, date)
→ Use [Regression Discontinuity]({{ site.baseurl }}/demos/Regression-Discontinuity-Toolkit.html)

### You're evaluating one treated unit (state, city, organization)
→ Use [Synthetic Control]({{ site.baseurl }}/demos/Synthetic-Control-Policy-Lab.html)

### You need to know who benefits most from an intervention
→ Use [Heterogeneous Treatment Effects]({{ site.baseurl }}/demos/Heterogeneous-Treatment-Effects.html)

### You're analyzing local labor markets
→ Use [Labor Market Intelligence]({{ site.baseurl }}/demos/Labor-Market-Intelligence.html)

### You're evaluating a federal place-based program
→ Use [Opportunity Zone Evaluation]({{ site.baseurl }}/demos/Opportunity-Zone-Evaluation.html)

### You need OMB-compliant cost-benefit analysis
→ Use [Workforce Development ROI]({{ site.baseurl }}/demos/Workforce-Development-ROI.html)
