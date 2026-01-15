---
title: Contributing
nav_order: 5
---

# Contributing

We welcome contributions that improve analytical quality, extend methodological coverage, or demonstrate new applications.

---

## What We're Looking For

### New analytical notebooks

Notebooks that meet the repository standards:

- Novel policy applications
- Alternative identification strategies
- Extensions to underserved domains (climate, criminal justice, education)
- Replications of published studies with improved methods

### Improvements to existing notebooks

- More efficient implementations
- Better visualization
- Clearer exposition
- Stronger robustness checks

### Documentation enhancements

- Clearer explanations of methodology
- Better guidance on when to use each approach
- Worked examples for specific policy questions

---

## What We're Not Looking For

- Notebooks that don't meet our methodological standards (we'll help you get there, but we won't merge weak identification strategies)
- Proprietary data that others can't access
- Methods that are purely descriptive when causal inference is feasible
- Analyses without proper uncertainty quantification

---

## How to Contribute

1. **Open an issue** describing what you want to add or improve
2. **Fork the repository** and create a branch
3. **Develop your contribution** following the existing structure and standards
4. **Submit a pull request** with clear documentation of what changed and why
5. **Engage in review discussion**—we'll work with you to meet quality thresholds

See [CONTRIBUTING.md](https://github.com/KhipuResearch/KASS/blob/main/CONTRIBUTING.md) in the repository for detailed guidelines, code style requirements, and review process.

---

## Notebook Requirements

Every notebook must include:

### Required Sections

1. **Title and Abstract** – What question does this answer?
2. **Motivation** – Why does this matter?
3. **Data** – Sources, access, limitations
4. **Methodology** – Identification strategy, assumptions
5. **Implementation** – Step-by-step code with explanation
6. **Results** – Findings with uncertainty quantification
7. **Robustness** – Alternative specifications, placebo tests
8. **Limitations** – What this can and can't tell us
9. **References** – Methodological and domain sources

### Code Standards

- Python 3.9+ compatible
- Type hints for functions
- Docstrings for non-obvious code
- Black formatting
- No hardcoded paths

---

## Discussion & Community

**Have questions about methodology?** Open a [Discussion](https://github.com/KhipuResearch/KASS/discussions) thread.

**Found a bug or methodological issue?** [Open an issue](https://github.com/KhipuResearch/KASS/issues).

**Want to collaborate?** We're particularly interested in applications to:

- State and local policy evaluation
- Equity impact assessment
- Climate adaptation analysis
- Workforce and labor market interventions
- Program evaluation in resource-constrained settings
