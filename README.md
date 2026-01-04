# KASS – KHIPU Analytics for Social Science

**Open-source notebooks demonstrating production-grade causal inference and policy analysis**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Discussions](https://img.shields.io/badge/GitHub-Discussions-181717?logo=github)](../../discussions)
[![Issues](https://img.shields.io/badge/Issues-Welcome-brightgreen)](../../issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

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

These notebooks represent the analytical backbone of the KRL platform. They're fully functional on their own, but they're also designed to show what becomes possible when you remove the grunt work from policy research.

---

## What's Inside

Each notebook solves a specific analytical problem using methods appropriate to the data structure and identification challenge:

### Causal Inference Methods

**[Heterogeneous Treatment Effects](notebooks/causal-inference/11-heterogeneous-treatment-effects.ipynb)**  
When average treatment effects hide more than they reveal. Uses causal forests and double machine learning to estimate how impacts vary across subpopulations—critical for targeting interventions and understanding equity implications.

**[Synthetic Control for Policy Evaluation](notebooks/causal-inference/14-synthetic-control-policy-lab.ipynb)**  
For situations where randomization is impossible and parallel trends are questionable. Constructs counterfactuals from weighted combinations of comparison units, with proper uncertainty quantification and placebo testing.

**[Regression Discontinuity Design](notebooks/causal-inference/15-regression-discontinuity-toolkit.ipynb)**  
Exploits policy thresholds to identify causal effects. Includes bandwidth selection algorithms, specification tests, and approaches for extrapolating beyond the discontinuity when necessary.

### Applied Policy Analysis

**[Labor Market Intelligence](notebooks/applied-econometrics/07-labor-market-intelligence.ipynb)**  
Integrates BLS, Census, and administrative data to identify skills gaps, wage dynamics, and structural changes in local labor markets. The kind of analysis workforce boards need but rarely have capacity to produce.

**[Opportunity Zone Evaluation](notebooks/applied-econometrics/20-opportunity-zone-evaluation.ipynb)**  
Comprehensive impact assessment of the federal Opportunity Zone program using difference-in-differences and synthetic controls. Examines effects on housing markets, business investment, and community outcomes—with attention to displacement and equity concerns.

**[Workforce Development ROI](notebooks/applied-econometrics/22-workforce-development-roi.ipynb)**  
Cost-benefit analysis for workforce programs that meets OMB Circular A-4 standards. Estimates earnings impacts, fiscal multipliers, and distributional effects using quasi-experimental methods and administrative earnings data.

---

## Standards & Methodology

Every notebook here adheres to specific quality thresholds:

**Identification Strategy**  
Clear statement of what variation identifies the causal effect, what assumptions are required, and what tests validate those assumptions.

**Robustness & Specification Tests**  
Not just one regression. Alternative specifications, placebo tests, sensitivity analyses, and honest discussion of what the results do and don't support.

**Reproducibility**  
Complete data pipelines from source to final result. If you can't reproduce it, it's not here.

**Honest Limitations**  
Every method has boundaries. We state them explicitly rather than hoping nobody notices.

**Audit & Remediation**  
All applied econometrics notebooks underwent independent audit in January 2026 and meet institutional standards for transparency, reproducibility, and methodological rigor. See [CHANGELOG.md](CHANGELOG.md) for remediation details.

These standards aren't about academic posturing—they're about producing analysis that decision-makers can actually rely on.

---

## How to Use This

**If you're learning causal inference:**  
Start with the method that matches your data structure. Each notebook includes detailed methodology sections explaining not just *how* to implement the estimator, but *why* the approach works and when it's appropriate.

**If you're conducting policy analysis:**  
Fork the repository, adapt the relevant notebook to your data and question, modify the specifications as needed. The code is structured to make this straightforward.

**If you're evaluating the KRL platform:**  
These notebooks demonstrate core analytical capabilities. The platform adds data connectivity, automated pipelines, collaboration features, and production-grade infrastructure around these methods.

**If you're contributing improvements:**
See [Contributing](#contributing) below. We're particularly interested in extensions that address new policy domains, alternative identification strategies, or methodological improvements.

---

## The KRL Connection

These notebooks are open-source demonstrations of analytical methods that KRL (Khipu Research Labs) implements at scale. The platform handles:

- **Data connectivity**: 68+ authoritative data sources (Census, BLS, CMS, state administrative data) with automated ETL
- **Model library**: 125+ causal inference models with proper documentation and validation
- **Collaborative infrastructure**: Team workspaces, audit trails, access controls suitable for government and research use
- **Reproducibility architecture**: Containerized environments, dependency management, computational reproducibility by default

If you find these notebooks useful but need to run hundreds of analyses rather than one, need institutional-grade infrastructure, or want to eliminate data acquisition overhead, that's what the platform provides.

[Learn more about KRL](https://krlabs.dev) | [Request beta access](https://krlabs.dev/beta)

---

## Contributing

We welcome contributions that improve analytical quality, extend methodological coverage, or demonstrate new applications:

### What We're Looking For

**New analytical notebooks** that meet the repository standards:
- Novel policy applications
- Alternative identification strategies
- Extensions to underserved domains (climate, criminal justice, education)
- Replications of published studies with improved methods

**Improvements to existing notebooks:**
- More efficient implementations
- Better visualization
- Clearer exposition
- Stronger robustness checks

**Documentation enhancements:**
- Clearer explanations of methodology
- Better guidance on when to use each approach
- Worked examples for specific policy questions

### What We're Not Looking For

- Notebooks that don't meet our methodological standards (we'll help you get there, but we won't merge weak identification strategies)
- Proprietary data that others can't access
- Methods that are purely descriptive when causal inference is feasible
- Analyses without proper uncertainty quantification

### How to Contribute

1. **Open an issue** describing what you want to add or improve
2. **Fork the repository** and create a branch
3. **Develop your contribution** following the existing structure and standards
4. **Submit a pull request** with clear documentation of what changed and why
5. **Engage in review discussion**—we'll work with you to meet quality thresholds

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines, code style requirements, and review process.

---

## Discussion & Community

**Have questions about methodology?** Open a [Discussion](../../discussions) thread. We're building a community of practice around rigorous policy analysis.

**Found a bug or methodological issue?** [Open an issue](../../issues). Transparent error correction is how we maintain credibility.

**Want to collaborate on a specific application?** Reach out through Discussions. We're particularly interested in applications to:
- State and local policy evaluation
- Equity impact assessment
- Climate adaptation analysis
- Workforce and labor market interventions
- Program evaluation in resource-constrained settings

**Looking for analytical support?** If you need help implementing these methods for your specific use case, we're building a community of practice. Join the discussion or explore what [KRL](https://krlabs.dev) can offer for production deployment.

---

## Technical Requirements

- **Python 3.9+**
- **Jupyter** or **JupyterLab**
- Key packages: `pandas`, `numpy`, `scipy`, `statsmodels`, `econml`, `causalml`, `matplotlib`, `seaborn`
- Data access (varies by notebook): Census API key, BLS API key, or administrative data access

See individual notebooks for specific environment requirements.

---

## Citation

If you use these notebooks in your research or operational work:

```bibtex
@software{kass2025,
  author = {Brandon Deloatch},
  title = {KASS: KHIPU Analytics for Social Science},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/bcdelodx/KASS}
}
```

And if you publish results derived from these methods, cite the original econometric papers referenced in each notebook.

---

## License

This repository is licensed under the **Apache License 2.0**.

You're free to use, modify, and distribute this code, including for commercial purposes. We only ask that you:
- Maintain proper attribution
- Share improvements back to the community when feasible
- Acknowledge methodological sources cited in the notebooks

See [LICENSE](LICENSE) for full terms.

---

## Roadmap

**Short-term additions** (Q1-Q2 2026):
- Spatial econometrics for regional policy analysis
- Event study designs with staggered treatment timing
- Bayesian methods for small-area estimation
- Instrumental variables toolkit with weak instrument diagnostics

**Medium-term goals** (Q3-Q4 2026):
- Machine learning for policy targeting
- Climate adaptation cost-benefit analysis
- Synthetic difference-in-differences
- Interactive dashboards for policy scenario analysis

**Long-term vision:**
Build a comprehensive open-source library of policy analysis methods that becomes the de facto standard for rigorous evidence-based decision-making.

Want to influence the roadmap? Join the [Discussions](../../discussions).

---

## Acknowledgments

These notebooks build on decades of econometric research and open-source software development. We're grateful to:

- The developers of `statsmodels`, `econml`, `causalml`, and related packages
- Academic researchers who publish replication materials
- Government statistical agencies who maintain open data APIs
- The broader community working toward better policy evidence

---

## Contact

**Questions?** [Open a Discussion](../../discussions)  
**Issues?** [Report them here](../../issues)  
**Collaborations?** [info@krlabs.dev](mailto:info@krlabs.dev)  
**Platform inquiries?** [https://krlabs.dev](https://krlabs.dev)

---

**Let's build better policy analysis infrastructure together.**
