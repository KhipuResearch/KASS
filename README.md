# KASS – KHIPU Analytics for Social Science

**Open-source notebooks demonstrating production-grade causal inference and policy analysis**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Discussions](https://img.shields.io/badge/GitHub-Discussions-181717?logo=github)](../../discussions)
[![Issues](https://img.shields.io/badge/Issues-Welcome-brightgreen)](../../issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## Status

- **Repository type:** External-facing demonstration. Six Jupyter notebooks plus
  a Jekyll-rendered Pages site. **Not a Python package** — no `pyproject.toml`,
  `setup.py`, `requirements.txt`, `environment.yml`, or `Pipfile` exists at the
  repository root.
- **Forensic SPEC of record:** [`SPEC.md`](SPEC.md) (894 lines), generated
  2026-04-23 against commit `27061e8a2d9b18bc1c2b6d06d0bf1deb3918bb19`.
- **Known gaps:** tracked in [`CALIBRATION_REQUIRED.md`](CALIBRATION_REQUIRED.md)
  and in three Architecture Decision Records under [`DECISIONS/`](DECISIONS/).
  The three most operationally consequential items are summarised below.
- **Test suite:** none ship with this repository. See
  [`tests/README.md`](tests/README.md) for the remediation path.

### Known Advisories (read before `pip install`)

1. **`requirements.txt` does not exist.** `README.md` (this file) and
   `docs/getting-started.md` both instruct users to run
   `pip install -r requirements.txt`, but the file has never been committed.
   First-time clones fail at that step. See
   [`DECISIONS/0002-missing-requirements-txt-gap.md`](DECISIONS/0002-missing-requirements-txt-gap.md)
   and the practical substitute in [Quick Start](#quick-start) below.
2. **The `krl_*` suite is not on public PyPI.** Every notebook imports at least
   one of `krl_core`, `krl_data_connectors`, `krl_models`, `krl_policy`,
   `krl_enterprise`, `krl_causal_policy`. Without `KRL_DEV_PATH` pointing to a
   private workspace, or platform credentials, the notebooks will not execute
   end-to-end. See
   [`DECISIONS/0001-demo-only-no-proprietary-compute.md`](DECISIONS/0001-demo-only-no-proprietary-compute.md).
3. **Pricing URL conflict.** The link to Stripe-integrated pricing in this
   README (line cited in `SPEC.md §16.5`) points at a personal-account host
   (`bcdelodx.github.io/KASS/pricing.html`) that is inconsistent with the
   organisation host used elsewhere (`khipuresearch.github.io/KASS/`). The
   canonical URL is **unresolved**. See
   [`DECISIONS/0003-pricing-url-conflict.md`](DECISIONS/0003-pricing-url-conflict.md).

---

## Documentation

**[View Full Documentation →](https://khipuresearch.github.io/KASS/)**

Architecture map: [`ARCHITECTURE.md`](ARCHITECTURE.md).
Policy-as-config stack: [`policy/`](policy/) (four YAML files — access,
secrets, dependency, CI authority).

---

## Interactive Demos

| Notebook | Method | View |
|----------|--------|------|
| Heterogeneous Treatment Effects | Causal Forests, Double ML | [View Demo →](https://khipuresearch.github.io/KASS/demos/Heterogeneous-Treatment-Effects.html) |
| Synthetic Control Policy Lab | Synthetic Control Method | [View Demo →](https://khipuresearch.github.io/KASS/demos/Synthetic-Control-Policy-Lab.html) |
| Regression Discontinuity Toolkit | RDD, Bandwidth Selection | [View Demo →](https://khipuresearch.github.io/KASS/demos/Regression-Discontinuity-Toolkit.html) |
| Labor Market Intelligence | BLS/Census Integration | [View Demo →](https://khipuresearch.github.io/KASS/demos/Labor-Market-Intelligence.html) |
| Opportunity Zone Evaluation | DiD, Synthetic Controls | [View Demo →](https://khipuresearch.github.io/KASS/demos/Opportunity-Zone-Evaluation.html) |
| Workforce Development ROI | Cost-Benefit Analysis | [View Demo →](https://khipuresearch.github.io/KASS/demos/Workforce-Development-ROI.html) |

Each link resolves to a **pre-rendered static HTML** export, not a runnable
notebook environment. There is no Binder or Colab integration — see
`SPEC.md §6.3`.

---

## Quick Start

```bash
git clone https://github.com/KhipuResearch/KASS.git
cd KASS
pip install -r requirements.txt     # ⚠ file does not exist — see ADR-0002
jupyter lab
```

**Practical substitute** (synthesised from notebook imports in `SPEC.md §4`):

```bash
pip install jupyter pandas numpy scipy scikit-learn \
            matplotlib seaborn plotly python-dotenv black
# ...plus private krl_* packages — KRL_DEV_PATH or platform credentials required
```

See [Getting Started](https://khipuresearch.github.io/KASS/getting-started) for
the fuller guide. Environment-variable contract lives in
[`policy/secrets.yaml`](policy/secrets.yaml); only `FRED_API_KEY` (all six
notebooks) and `BLS_API_KEY` (NB07) are required of the user directly.

---

## What This Is

KASS is a curated set of Jupyter notebooks that tackle real policy questions
using rigorous causal inference methods. These aren't toy examples. They're
the kind of analyses that federal agencies, research institutions, and policy
shops actually run — complete with proper identification strategies,
robustness checks, and transparent limitations.

Think of this repository as:

- **A showcase** of what's possible with modern econometric methods
- **A learning resource** for applied researchers who need to estimate causal effects
- **A technical proof-of-concept** for the [KRL (Khipu Research Labs)](https://krlabs.dev) platform

If you've ever struggled with messy policy data, debated whether your
treatment effects are believable, or wondered whether your regression
discontinuity design would survive peer review, you're in the right place.

---

## Why This Exists

Policy analysis has a credibility problem. Too much of what passes for
"evaluation" relies on correlations dressed up as causation. Too many
decisions get made on gut feeling because rigorous analysis takes too long.
And too many researchers waste time rebuilding analytical infrastructure that
should be standardized by now.

We built KASS to demonstrate what changes when you have:

- **Proper causal inference methodologies** baked into your workflow
- **Direct access to authoritative data sources** (Census, BLS, administrative records)
- **Reproducible pipelines** that anyone can audit and extend

These notebooks represent the analytical backbone of the KRL platform. They're
fully functional on their own, but they're also designed to show what becomes
possible when you remove the grunt work from policy research.

---

## What's Inside

Each notebook solves a specific analytical problem using methods appropriate
to the data structure and identification challenge:

### Causal Inference Methods

**[Heterogeneous Treatment Effects](notebooks/causal-inference/11-heterogeneous-treatment-effects.ipynb)**
When average treatment effects hide more than they reveal. Uses causal forests
and double machine learning to estimate how impacts vary across
subpopulations — critical for targeting interventions and understanding equity
implications.

**[Synthetic Control for Policy Evaluation](notebooks/causal-inference/14-synthetic-control-policy-lab.ipynb)**
For situations where randomization is impossible and parallel trends are
questionable. Constructs counterfactuals from weighted combinations of
comparison units, with proper uncertainty quantification and placebo testing.

**[Regression Discontinuity Design](notebooks/causal-inference/15-regression-discontinuity-toolkit.ipynb)**
Exploits policy thresholds to identify causal effects. Includes bandwidth
selection algorithms, specification tests, and approaches for extrapolating
beyond the discontinuity when necessary.

### Applied Policy Analysis

**[Labor Market Intelligence](notebooks/applied-econometrics/07-labor-market-intelligence.ipynb)**
Integrates BLS, Census, and administrative data to identify skills gaps, wage
dynamics, and structural changes in local labor markets.

**[Opportunity Zone Evaluation](notebooks/applied-econometrics/20-opportunity-zone-evaluation.ipynb)**
Comprehensive impact assessment of the federal Opportunity Zone program using
difference-in-differences and synthetic controls. Carries a **hybrid-data
disclosure** (real FRED county data blended with pre-programmed treatment
effects) per `CHANGELOG.md:58-63`.

**[Workforce Development ROI](notebooks/applied-econometrics/22-workforce-development-roi.ipynb)**
Cost-benefit analysis for workforce programs that meets OMB Circular A-4
standards. Carries a **methodological-demonstration** disclosure
(pre-programmed effects) per `CHANGELOG.md:47-54`.

---

## Standards & Methodology

Every notebook here adheres to specific quality thresholds:

- **Identification strategy** — explicit statement of what variation
  identifies the causal effect, what assumptions are required, and what tests
  validate those assumptions.
- **Robustness & specification tests** — alternative specifications, placebo
  tests, sensitivity analyses, and honest discussion of what the results do
  and don't support.
- **Reproducibility** — complete data pipelines from source to final result.
  If you can't reproduce it, it's not here.
- **Honest limitations** — every method has boundaries; they are stated
  explicitly.
- **Audit & remediation** — all applied econometrics notebooks underwent
  independent audit in January 2026. See [`CHANGELOG.md`](CHANGELOG.md).

These standards are enforced by human review, not by an automated test
harness. See [`tests/README.md`](tests/README.md) for the remediation plan.

---

## How to Use This

**If you're learning causal inference:** start with the method that matches
your data structure. Each notebook includes detailed methodology sections
explaining not just *how* to implement the estimator, but *why* the approach
works and when it's appropriate.

**If you're conducting policy analysis:** fork the repository, adapt the
relevant notebook to your data and question, modify the specifications as
needed.

**If you're evaluating the KRL platform:** these notebooks demonstrate core
analytical capabilities. The platform adds data connectivity, automated
pipelines, collaboration features, and production-grade infrastructure.

**If you're contributing improvements:** see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## The KRL Connection

These notebooks are open-source demonstrations of analytical methods that KRL
(Khipu Research Labs) implements at scale. Repository-level accuracy of the
two most-quoted platform statistics — "68+ authoritative data sources" and
"125+ causal inference models" — cannot be verified from this repository
alone; both are proprietary-platform claims (`SPEC.md §16.8`). The notebooks
reachable here cover two public APIs (FRED and BLS) and six methods.

[Learn more about KRL](https://krlabs.dev) | [Request beta access](https://krlabs.dev/beta)

---

## Platform Access & Pricing

| Tier | Monthly Cost | API Calls | Best For |
|------|--------------|-----------|----------|
| **Community** | **Free** | 10,000 | Learning, teaching, exploratory analysis. Full model zoo access. |
| **Professional** | **$149** | 100,000 | Individual researchers and small teams running regular policy analysis. |
| **Team** | **$499** + per seat | Custom | Research shops, consultancies, policy units. |
| **Enterprise** | **Custom** | Unlimited | Government agencies, large institutions. |

**Current Status:** Beta. SOC 2 Type II certification expected Q2 2026.

### [View Interactive Pricing & Subscribe →](https://bcdelodx.github.io/KASS/pricing.html)

> ⚠ The host of the link above (`bcdelodx.github.io`) conflicts with the
> organisation host used by this repository's Jekyll site
> (`khipuresearch.github.io`). The canonical pricing URL is **unresolved** —
> see [`DECISIONS/0003-pricing-url-conflict.md`](DECISIONS/0003-pricing-url-conflict.md).
> The Stripe Payment Link URLs enumerated in `CHANGELOG.md:13-17` are
> likewise documented placeholders.

---

## Contributing

Contributions that improve analytical quality, extend methodological coverage,
or demonstrate new applications are welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md) for code-style requirements, notebook
quality gates, and the review process.

All contributors must observe:

- [`policy/access-control.yaml`](policy/access-control.yaml) — who can merge.
- [`policy/dependency.yaml`](policy/dependency.yaml) — dependency-surface
  rules, including how to add a package to the (yet-to-exist)
  `requirements.txt`.
- [`policy/secrets.yaml`](policy/secrets.yaml) — no secrets in code;
  environment-variable list.

---

## Discussion & Community

- **Questions about methodology** — open a [Discussion](../../discussions).
- **Bugs or methodological issues** — [open an issue](../../issues).

---

## Technical Requirements

- **Python 3.9+**
- **Jupyter** or **JupyterLab**
- Third-party PyPI packages actually imported by the notebooks: `pandas`,
  `numpy`, `scipy`, `scikit-learn`, `matplotlib`, `seaborn`, `plotly`,
  `python-dotenv`. (`statsmodels`, `econml`, `causalml` are named in
  `CONTRIBUTING.md:37` but not imported by any committed notebook —
  `SPEC.md §16.8`.)
- Private `krl_*` packages — not publicly installable.
- Data access: FRED API key (all notebooks); BLS API key (NB07).

See individual notebooks for specific environment requirements.

---

## Citation

```bibtex
@software{kass2025,
 author = {Brandon Deloatch},
 title = {KASS: KHIPU Analytics for Social Science},
 year = {2025},
 publisher = {GitHub},
 url = {https://github.com/bcdelodx/KASS}
}
```

---

## License

This repository is licensed under the **Apache License 2.0**. See
[LICENSE](LICENSE).

---

## Roadmap

Forward-looking items previously enumerated in this section depend on
decisions still open in [`DECISIONS/`](DECISIONS/) and
[`CALIBRATION_REQUIRED.md`](CALIBRATION_REQUIRED.md). The section will be
restored once a public-installable variant (ADR-0001) and a committed
`requirements.txt` (ADR-0002) make the short-term items executable.

---

## Contact

- **Questions** — [Open a Discussion](../../discussions)
- **Issues** — [Report them here](../../issues)
- **Collaborations** — <info@krlabs.dev>
- **Security** — <security@krlabs.dev> ([SECURITY.md](SECURITY.md))

---

**Let's build better policy analysis infrastructure together.**
