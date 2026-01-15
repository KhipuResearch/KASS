---
title: Methodology
nav_order: 4
---

# Standards & Methodology

Every notebook in KASS adheres to specific quality thresholds. These standards aren't about academic posturing—they're about producing analysis that decision-makers can actually rely on.

---

## Identification Strategy

Clear statement of what variation identifies the causal effect, what assumptions are required, and what tests validate those assumptions.

Every notebook answers:

- What is the source of identifying variation?
- What assumptions are required for causal interpretation?
- How do we test those assumptions?
- What would invalidate the analysis?

---

## Robustness & Specification Tests

Not just one regression. Alternative specifications, placebo tests, sensitivity analyses, and honest discussion of what the results do and don't support.

Standard robustness checks include:

- **Alternative bandwidths** (for RD designs)
- **Different functional forms** (linear, polynomial, nonparametric)
- **Placebo outcomes** (variables that shouldn't be affected)
- **Placebo treatments** (times/places without treatment)
- **Sensitivity to unobservables** (Oster bounds, Rosenbaum bounds)

---

## Reproducibility

Complete data pipelines from source to final result. If you can't reproduce it, it's not here.

Requirements:

- All data acquisition code included
- Random seeds set for stochastic methods
- Environment specifications provided
- Results regenerate identically

---

## Honest Limitations

Every method has boundaries. We state them explicitly rather than hoping nobody notices.

Each notebook includes:

- **External validity**: Where do these results generalize?
- **Internal validity threats**: What could bias the estimates?
- **Data limitations**: What's missing or measured with error?
- **Policy applicability**: What can and can't this analysis inform?

---

## Audit & Remediation

All applied econometrics notebooks underwent independent audit in January 2026 and meet institutional standards for transparency, reproducibility, and methodological rigor.

See [CHANGELOG.md](https://github.com/KhipuResearch/KASS/blob/main/CHANGELOG.md) for remediation details.

### Audit Outcomes

| Notebook | Pre-Audit Grade | Post-Audit Grade |
|----------|-----------------|------------------|
| Labor Market Intelligence (NB07) | C+ | A- |
| Opportunity Zone Evaluation (NB20) | B+ | A |
| Workforce Development ROI (NB22) | B+ | A- |

---

## Quality Checklist

Before any notebook is merged, it must satisfy:

- [ ] Clear identification strategy documented
- [ ] At least 3 robustness checks implemented
- [ ] All code executes without modification
- [ ] Limitations section is substantive
- [ ] Data sources are publicly accessible (or synthetic alternatives provided)
- [ ] Results interpretation is conservative
