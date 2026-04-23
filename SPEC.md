# SPEC — KASS (KHIPU Analytics for Social Science)

> **Status:** Forensic specification generated from repository evidence.
> **Generated:** 2026-04-23 from commit `27061e8a2d9b18bc1c2b6d06d0bf1deb3918bb19` on branch `main`.
> **Scope:** External-facing open-source demonstration repository. Six Jupyter
> notebooks showcasing production-grade causal inference and policy analysis
> built atop the proprietary KRL Suite. **Not a Python package** — no
> `pyproject.toml`, `setup.py`, `requirements.txt`, `environment.yml`, or
> `Pipfile` exists at the repository root or anywhere in the tree.

---

## 1. Purpose & Positioning

KASS is the public, Apache-2.0-licensed demonstration surface for Khipu Research
Labs' proprietary analytics platform. Its stated purpose (`README.md:48-56`) is
three-fold: (a) showcase modern econometric methods, (b) serve as a learning
resource for applied causal inference, and (c) act as a technical
proof-of-concept funnel for the commercial KRL platform.

The repository's own framing (`README.md:3`) is:

> Open-source notebooks demonstrating production-grade causal inference and
> policy analysis

It is explicitly **not** a library or framework. `README.md:131-135` directs
users who want production scale to the KRL platform itself:

> These notebooks demonstrate core analytical capabilities. The platform adds
> data connectivity, automated pipelines, collaboration features, and
> production-grade infrastructure around these methods.

Downstream links (`README.md:183`) push toward
`https://bcdelodx.github.io/KASS/pricing.html`, and every notebook ends with a
"KRL Suite Components & Pricing" section, making this a hybrid demo-plus-funnel
artifact rather than a neutral reference implementation.

### 1.1 Intended Audience & Non-Goals

Audiences: applied researchers (`README.md:125-127`); policy analysts
(`README.md:128-129`); KRL platform evaluators (`README.md:131-133`);
government agencies needing OMB-A-4-grade output (`CONTRIBUTING.md:170-175`).

Non-goals: not a Python package (no install artifacts, no PyPI); not a full
platform (the platform is paid, `README.md:143-148`); not for proprietary-data
analyses (`README.md:217`).

---

## 2. High-Level Architecture

The repository has four parallel layers:

| Layer | Location | Purpose |
|-------|----------|---------|
| Notebooks (content) | `notebooks/` | Six `.ipynb` demonstrations organized by domain |
| Rendered output | `notebook_results/`, `docs/demos/` | Pre-executed HTML exports for web publication |
| Jekyll site | `docs/` | GitHub Pages documentation site ("Just the Docs" theme) |
| Governance | `.github/`, `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE`, `SECURITY.md` | Repository policy, templates, workflows |

There is a fifth transient layer — internal staging directories
(`KASS_Discussion_Labels/`, `KASS_Issues/`, `KASS_Pull_Template/`) plus the
`KASS_NOTEBOOK_*.md` directives — explicitly listed in `.gitignore:61-65` as
"Internal staging files (already deployed to .github/)". These represent
single-shot migration scaffolding, not runtime artefacts.

The notebooks themselves depend on a **private, external** KRL Suite
(`krl_core`, `krl_data_connectors`, `krl_models`, `krl_policy`, `krl_enterprise`,
`krl_causal_policy`). That suite is not in this repository and cannot be
installed from PyPI without credentials — notebook imports fail outside a
configured KRL environment (see §4).

---

## 3. Tech Stack

### 3.1 Runtime

| Component | Evidence | Notes |
|-----------|----------|-------|
| Python 3.9+ | `README.md:252`, `CONTRIBUTING.md:30` | Minimum version asserted in README badge and Contributing guide |
| Jupyter / JupyterLab | `README.md:253`, `CONTRIBUTING.md:37` | Execution runtime |
| Kernel display name | `metadata.kernelspec` in every `.ipynb` | All six notebooks tag `".venv-workspace"` as the development kernel |
| Jekyll 4.3 | `docs/Gemfile:3` | Documentation site build |
| just-the-docs 0.10 | `docs/Gemfile:4`, `docs/_config.yml:8` | Jekyll theme |
| Ruby 3.2 | `.github/workflows/pages.yml:30` | Pages CI runtime |

### 3.2 Dependency Declaration — **Absent at Repository Level**

There is **no dependency manifest** in this repository. Verification:

```
find /Users/bcdelo/Documents/GitHub/KRL/KASS \
  -name 'requirements*.txt' -o -name 'pyproject.toml' \
  -o -name 'environment.yml'  -o -name 'setup.py' \
  -o -name 'Pipfile*'         -o -name 'poetry.lock'
```

Returns **zero** results outside `.git/`. Despite this, `README.md:38` and
`docs/getting-started.md:28-30` both instruct users to run:

```bash
pip install -r requirements.txt
```

This is a documented gap — the file does not exist. Users must synthesise
dependencies from imports (§4). The `PULL_REQUEST_TEMPLATE.md:69` checklist
item "Requirements.txt updated if new packages added" reinforces an intended
but unrealised convention.

### 3.3 Per-Notebook Dependencies (extracted from imports)

The only programmatic source of truth for dependencies is the import lattice of
the six notebooks. Common third-party packages across all six:

| Package | Used in |
|---------|---------|
| `pandas`, `numpy`, `matplotlib.pyplot`, `seaborn`, `scipy` | All 6 notebooks |
| `python-dotenv` (`from dotenv import load_dotenv`) | All 6 |
| `scikit-learn` (`sklearn.*`) | 5 of 6 (not NB14 standalone) |
| `plotly.express`, `plotly.graph_objects`, `plotly.subplots` | 5 of 6 (absent NB07) |

Notebook-specific: see §15.

### 3.4 KRL Proprietary Modules (all imported, none packaged here)

Evidence from notebook import analysis:

| Module | Used in |
|--------|---------|
| `krl_core.get_logger` | All 6 |
| `krl_data_connectors.skip_license_check` | NB20, NB22, NB11, NB14 |
| `krl_data_connectors.community.*` | NB07 |
| `krl_data_connectors.professional.fred_full.FREDFullConnector` | NB20, NB22 |
| `krl_data_connectors.professional.FREDFullConnector` | NB11, NB14 |
| `krl_models.{LocationQuotientModel, ShiftShareModel, STLAnomalyModel}` | NB07 |
| `krl_enterprise.OpportunityZoneEvaluator` | NB20 |
| `krl_enterprise.WorkforceROICalculator` | NB22 |
| `krl_policy.enterprise.DoubleML` | NB11 |
| `krl_causal_policy.enterprise.MultiUnitSCM` | NB14 |
| `krl_causal_policy.enterprise.{MulticutoffRDD, RDKink}` | NB15 |

Bootstrap strategy (`notebooks/causal-inference/14-synthetic-control-policy-lab.ipynb`,
first code cell, recoverable via `jq -r '.cells[] | select(.cell_type=="code") | .source | join("")' <file> | head -60`):

- If `KRL_DEV_PATH` env var is set and points to a checkout of the private
  `Private IP/` workspace, local `src/` paths are prepended to `sys.path`.
- Otherwise the notebook falls back to pip-installed `krl-core`, 
  `krl-data-connectors`, and `krl-causal-policy-toolkit` — packages which are
  **not** on public PyPI and require platform credentials.

### 3.5 Style Tooling

- `black` declared as formatter (`README.md:7` badge, `CONTRIBUTING.md:191-193`,
  `CONTRIBUTING.md:270`)
- PEP 8 line length 88 (`CONTRIBUTING.md:193`)
- No `.flake8`, `pyproject.toml`, `ruff.toml`, or `.black.toml` present — style
  rules are documentary, not automated.

---

## 4. Dependency Map (Best-Effort from Imports)

With no manifest, this map is reconstructed per-notebook. Third-party PyPI
packages first, then KRL suite, then stdlib (elided unless notable).

### NB07 — Labor Market Intelligence

```
pandas, numpy, scipy.stats (pearsonr, stats), matplotlib, seaborn,
sklearn.preprocessing.MinMaxScaler, python-dotenv
krl_core.get_logger
krl_data_connectors.community.*
krl_models.{LocationQuotientModel, ShiftShareModel, STLAnomalyModel}
```

Env vars required: `BLS_API_KEY`, `FRED_API_KEY`. After Jan 2026 audit,
`CHANGELOG.md:40` states demo-data fallbacks were removed — missing keys now
raise `RuntimeError`.

### NB20 — Opportunity Zone Evaluation

```
pandas, numpy, scipy.stats, matplotlib (+ matplotlib.patches), seaborn,
plotly (express, graph_objects, subplots), python-dotenv,
sklearn.linear_model.LogisticRegression, sklearn.preprocessing.StandardScaler
krl_core.get_logger
krl_data_connectors.skip_license_check
krl_data_connectors.professional.fred_full.FREDFullConnector
krl_enterprise.OpportunityZoneEvaluator
```

Env var: `FRED_API_KEY`.

### NB22 — Workforce Development ROI

```
Same third-party set as NB20, plus
sklearn.linear_model.{LinearRegression, LogisticRegression},
sklearn.neighbors.NearestNeighbors
krl_enterprise.WorkforceROICalculator
```

Env var: `FRED_API_KEY`.

### NB11 — Heterogeneous Treatment Effects

```
pandas, numpy, scipy.stats, matplotlib, seaborn,
plotly (express, graph_objects, subplots), python-dotenv,
sklearn.ensemble.{RandomForestRegressor, GradientBoostingRegressor},
sklearn.linear_model.LogisticRegression,
sklearn.model_selection.cross_val_predict
krl_core.get_logger
krl_data_connectors.skip_license_check
krl_data_connectors.professional.FREDFullConnector
krl_policy.enterprise.DoubleML
```

Env var: `FRED_API_KEY`.

### NB14 — Synthetic Control Policy Lab

```
pandas, numpy, scipy.optimize, scipy.stats (aliased scipy_stats),
scipy.stats.linregress, matplotlib, seaborn,
plotly (express, graph_objects, subplots), python-dotenv,
sklearn.preprocessing.StandardScaler
krl_core.get_logger
krl_data_connectors.skip_license_check
krl_data_connectors.professional.FREDFullConnector
krl_causal_policy.enterprise.MultiUnitSCM
```

Env var: `FRED_API_KEY`.

### NB15 — Regression Discontinuity Toolkit

```
pandas, numpy, scipy.stats, scipy.optimize, matplotlib, seaborn,
plotly (express, graph_objects, subplots), python-dotenv,
sklearn.linear_model.LinearRegression,
sklearn.preprocessing.PolynomialFeatures
krl_core.get_logger
krl_causal_policy.enterprise.{MulticutoffRDD, RDKink}
```

Env var: `FRED_API_KEY`.

### 4.1 Implied Tier Access

`fix_badges.py:17-25` records the tier taxonomy the notebooks target:

| Notebook | Tier | Data |
|----------|------|------|
| NB07 | Community | BLS + FRED |
| NB14 | Community | FRED State Economics |
| NB15 | Community | FRED County Economics |
| NB20 | Professional | FRED County Economics |
| NB22 | Professional | FRED Labor Market |
| NB11 | Pro + Enterprise | FRED State Economics |

Checkout links (`CHANGELOG.md:12-17`) point at Stripe Payment Links — the
$5/hour, $15/day, $99/week, $149/month, $1,428/year levels are the live KRL
pricing surface for users who hit a tier gate.

---

## 5. Repository Layout

```
KASS/                                    71 tracked files (excl. .git/.ipynb_checkpoints)
├── .github/                             GitHub governance
│   ├── CODE_OF_CONDUCT.md
│   ├── FUNDING.yml                     Ko-fi=Khipu (only populated field)
│   ├── ISSUE_TEMPLATE/                 6 templates: bug, config, data connector,
│   │   │                               docs, feature, notebook improvement
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── SECURITY.md
│   └── workflows/
│       ├── issue-management.yml        Auto-label, welcome, remove needs-triage
│       ├── pages.yml                   Jekyll build + deploy to GH Pages
│       └── stale.yml                   30-day stale, 14-day close
├── .gitignore
├── CHANGELOG.md                        87 lines — audit & graceful-degradation log
├── CONTRIBUTING.md                     481 lines
├── KASS_Discussion_Labels/             (gitignored) internal label-migration tooling
├── KASS_Issues/                        (gitignored) internal issue-template staging
├── KASS_NOTEBOOK_PRACTICAL_WORKFLOW.md  1,273 lines, gitignored directive
├── KASS_NOTEBOOK_UPDATE_DIRECTIVE.md    1,446 lines, gitignored directive
├── KASS_Pull_Template/                 (gitignored) internal PR-template staging
├── LICENSE                             Apache License 2.0 (201 lines)
├── README.md                           332 lines
├── data/                               EMPTY directory (ls shows only .DS_Store parent)
├── docs/                               Jekyll site (GitHub Pages)
│   ├── Gemfile                         jekyll ~> 4.3, just-the-docs ~> 0.10
│   ├── _config.yml                     baseurl=/KASS, color_scheme=millennial
│   ├── _sass/color_schemes/millennial.scss
│   ├── _sass/custom/custom.scss
│   ├── about.md, getting-started.md, index.md, methodology.md
│   ├── assets/images/                  EMPTY
│   ├── demos/                          6 HTML files (rendered notebook previews)
│   └── notebooks/                      7 markdown pages (one per notebook + index)
├── fix_badges.py                       69 lines — one-shot badge-rewrite script
├── notebook_results/                   6 pre-rendered HTML files (4.5 MB total)
├── notebooks/
│   ├── applied-econometrics/
│   │   ├── 07-labor-market-intelligence.ipynb      (272 KB, 28 cells)
│   │   ├── 20-opportunity-zone-evaluation.ipynb    (996 KB, 32 cells)
│   │   └── 22-workforce-development-roi.ipynb      (211 KB, 32 cells)
│   └── causal-inference/
│       ├── 11-heterogeneous-treatment-effects.ipynb (1.77 MB, 32 cells)
│       ├── 14-synthetic-control-policy-lab.ipynb    (250 KB, 26 cells)
│       └── 15-regression-discontinuity-toolkit.ipynb (301 KB, 26 cells)
└── pricing.html                        293 lines — standalone Stripe-linked pricing page
```

File-type tally (excluding `.git/`):

| Extension | Count |
|-----------|-------|
| `.md` | 22 |
| `.html` | 13 (6 in `docs/demos/` + 6 in `notebook_results/` + 1 root `pricing.html`) |
| `.yml` | 7 (3 workflows + 5 issue templates + FUNDING + 1 deploy script config) |
| `.ipynb` | 6 |
| `.sh` | 3 (internal staging only; all gitignored) |
| `.scss` | 2 |
| `.py` | 1 (`fix_badges.py` only — it is not a notebook, module, or package) |

The 603-file claim in the task brief is not corroborated — `find` reports 71
tracked files excluding `.git/` and `.ipynb_checkpoints/`. The discrepancy
likely counts `.git/` internals or dropped-output notebook cells separately.

---

## 6. Build & Run

### 6.1 Notebook Execution (intended workflow)

From `README.md:33-40`:

```bash
git clone https://github.com/KhipuResearch/KASS.git
cd KASS
pip install -r requirements.txt     # <-- FILE DOES NOT EXIST
jupyter lab
```

A user following these instructions literally will hit
`ERROR: Could not open requirements file: [Errno 2] No such file or directory`.
The practical substitute, assembled from `CONTRIBUTING.md:35-38`:

```bash
pip install jupyter pandas numpy scipy statsmodels econml causalml \
            matplotlib seaborn black
```

(Note: `statsmodels`, `econml`, `causalml` are listed by Contributing but
**none of the six notebooks actually import them** — they appear as
aspirational / advertised dependencies, not runtime ones. Every notebook does,
however, require the KRL suite which is not covered by any of the above.)

### 6.2 Environment Variables

`.env` lookup order (`notebooks/causal-inference/14-synthetic-control-policy-lab.ipynb`
first code cell, lines ~21-24 within cell):

1. `~/.krl/.env`
2. `./.env`

Required keys (per §4): `FRED_API_KEY` (all six notebooks), `BLS_API_KEY`
(NB07 only). Developers on the KRL team can set `KRL_DEV_PATH` to skip pip
install entirely and import from a local `Private IP/` workspace.

### 6.3 Binder / Colab

**Not applicable.** No `binder/` directory, no `postBuild` script, no Colab
badges, no `.binder` config file. Despite `README.md:20-29` listing a table of
"Interactive Demos," each link routes to a **pre-rendered HTML** view at
`khipuresearch.github.io/KASS/demos/<Notebook>.html`, not a runnable notebook.
Interactive execution is gated on local install + KRL platform credentials.

### 6.4 Documentation Site

The Jekyll site builds via GitHub Actions (`.github/workflows/pages.yml:17-59`):

1. Checkout, setup Ruby 3.2
2. `cd docs && bundle install`
3. `bundle exec jekyll build --baseurl /KASS`
4. Upload artefact, deploy to `github-pages` environment

Triggered on push to `main` or manual dispatch. `concurrency: pages` prevents
overlapping deploys. There is no `Gemfile.lock` checked in (see commit
`4f8def8: Fix Jekyll build: remove lockfile, let CI generate dependencies`).

### 6.5 Output Regeneration

The six HTML files in `notebook_results/` and `docs/demos/` are produced
outside CI — there is no `nbconvert` workflow in `.github/workflows/`. Dates on
`notebook_results/*.html` (Jan 8, 2026) predate the Feb 13 "notebook updates"
commit, implying the published demos may drift from notebook source between
manual regenerations.

---

## 7. Configuration

### 7.1 Jekyll (`docs/_config.yml`)

| Key | Value |
|-----|-------|
| `title` | KASS |
| `url` | https://khipuresearch.github.io |
| `baseurl` | /KASS |
| `theme` | just-the-docs |
| `color_scheme` | millennial |
| `search_enabled` | true |
| `aux_links.GitHub` | https://github.com/KhipuResearch/KASS |

### 7.2 Theme Customisation

- `docs/_sass/color_schemes/millennial.scss` (981 B) — colour scheme override
- `docs/_sass/custom/custom.scss` (3.3 KB) — layout / typography overrides
- `docs/assets/images/` — empty

### 7.3 Stale-Bot Tuning (`.github/workflows/stale.yml`)

Issues: 30 days to stale, +14 to close. PRs: 45 days to stale, +14 to close.
Exempt labels: `priority-urgent`, `priority-high`, `in-progress`, `blocked`,
`good-first-issue`, `help-wanted`, `enhancement`. `exempt-all-milestones: true`.

### 7.4 Issue Auto-Labelling (`.github/workflows/issue-management.yml`)

Keyword rules (lines 90-120) add method-tagged labels (`method-did`,
`method-synth-control`, `method-rdd`, `method-hte`, `method-iv`,
`method-matching`) and domain-tagged labels (`domain-workforce`,
`domain-education`, `domain-health`, `domain-housing`, `domain-environment`,
`domain-justice`, `domain-economic`).

---

## 8. API Contracts

**Not applicable.** KASS is a demonstration repository with no HTTP server, no
CLI, no SDK, no exported public Python API, and no JSON-schema or OpenAPI
artifact. The notebooks *consume* the FRED and BLS public REST APIs via the
proprietary `krl_data_connectors` package (not vendored here), but do not
expose any callable endpoints of their own.

The only reachable URLs this repository *publishes* are:

- Jekyll pages under `https://khipuresearch.github.io/KASS/*` — plain static
  HTML, no contract.
- Pre-rendered notebook HTML under `.../demos/*.html` — static snapshots.
- Stripe Payment Links referenced in `CHANGELOG.md:13-17`. These are
  documented placeholder URLs (`README.md:20` of CHANGELOG: "Replace
  placeholder URLs with actual Stripe Payment Links from your dashboard").

The public-facing API in the marketing sense is the KRL Platform
(`krlabs.dev`), which is not hosted, specified, or implemented by this
repository.

---

## 9. Data Model

### 9.1 `data/` directory

Empty. `ls -la data/` shows `.` and `..` only. `.gitignore:31-37` excludes all
data file types (`*.csv`, `*.xlsx`, `*.parquet`, `*.h5`, `*.hdf5`) and the
entire `data/` directory, with an allowlist exception for
`!notebooks/**/sample_data.csv`. No such `sample_data.csv` exists in the tree.

### 9.2 Runtime Data Sources (consumed, not stored)

Each notebook pulls live data via FRED (Federal Reserve Economic Data) and/or
BLS APIs through the `krl_data_connectors` shim. This is the only persistence
surface; `README.md:62-65` asserts:

> Direct access to authoritative data sources (Census, BLS, administrative
> records)

Audit hardening (`CHANGELOG.md:40`, NB07 row) removed demo-data fallbacks so
execution now requires live API access:

> FIXED: Removed demo data fallbacks (now requires valid API keys with
> RuntimeError on failure)

NB20 uniquely carries a "HYBRID DATA STRUCTURE NOTICE" (top markdown section
per H2 header scan) — it blends real FRED county data with pre-programmed
simulated treatment effects, a remediated disclosure per `CHANGELOG.md:58-63`.

### 9.3 Intermediate Artifacts

- `notebook_results/*.html`: 6 files, 0.5–1.2 MB each, representing full
  executed notebook runs with embedded figures. These are source-of-truth for
  the rendered demos at `docs/demos/*.html`.
- No cached pickles, no Parquet outputs, no database migrations.

### 9.4 Schema Contracts

None. The notebooks operate on DataFrames pulled at runtime; there is no
schema definition file, dbt model, Pydantic schema, or Avro/Protobuf artefact.

---

## 10. Authentication & Authorization

The repository has no auth layer of its own. What exists instead is a *tier
gate* inside the proprietary KRL libraries, which fails gracefully inside the
notebooks when a Community-tier user invokes a Pro or Enterprise feature.

From `CHANGELOG.md:5-20`:

> When a notebook tries to import a tier-restricted feature:
> - Displays clear upgrade banner with feature description
> - Shows current vs. required tier information (COMMUNITY → PROFESSIONAL →
>   ENTERPRISE)
> - Direct Stripe Payment Links for instant checkout
> - Falls back gracefully where possible (e.g., FREDBasicConnector for
>   community)

API-key handling (`CHANGELOG.md:40` and per-notebook analysis): all secrets
come from environment variables loaded by `python-dotenv`. No hardcoded keys
anywhere. `.gitignore:40-41` excludes `.env` and `.venv`.

---

## 11. Security

### 11.1 Declared Policy (`.github/SECURITY.md`)

- Private disclosure to `security@krlabs.dev` (line 18)
- Acknowledgement target: 48 hours (line 28)
- Assessment target: 7 days (line 29)
- Fix timeline: severity-dependent (line 30)
- 90-day public disclosure window (line 82)

### 11.2 Best-Practice Guidance (SECURITY.md:46-74)

- Never commit credentials; use env vars + `.env` in `.gitignore`
- Validate data-source URLs and SSL
- Use `pip-audit` to check dependencies
- No real PII in example notebooks
- Enable SSO + 2FA on the KRL platform

### 11.3 Enforcement (none automated in this repo)

No dependency scanning workflow, no CodeQL, no SAST/DAST, no `pre-commit`
config. Security is policy-by-documentation. A `pip-audit` run is recommended
(SECURITY.md:62) but not wired up.

### 11.4 Secrets Surface

- Repository greps clean for hardcoded keys: only `os.getenv('FRED_API_KEY')`,
  `os.getenv('BLS_API_KEY')` patterns appear, plus error messages instructing
  users to set those vars.
- No `.env.example` ships — users must consult `CONTRIBUTING.md:42-44` for
  signup links.

---

## 12. Observability

**Not applicable for the repository itself.** There is no application to
observe. What exists is internal logging at the notebook level via
`krl_core.get_logger` (used by all six notebooks) — a proprietary wrapper
whose behaviour is defined outside this repo.

No metrics, traces, dashboards, or error-tracking integrations ship here.

---

## 13. Testing Strategy

KASS carries **no automated tests**. Evidence:

- No `tests/` directory at any depth.
- No `test_*.py` or `*_test.py` files.
- No `pytest.ini`, `tox.ini`, `conftest.py`, `noxfile.py`.
- No test-related workflow (`.github/workflows/` contains only `pages.yml`,
  `issue-management.yml`, `stale.yml`).
- `fix_badges.py` is a one-shot migration script, not a test.

The only quality discipline is **manual notebook execution** before merge
(`CONTRIBUTING.md:271-272`):

> 3. Format your code: `black your_notebook.ipynb`
> 4. Clear all outputs (for clean diffs):
>    `jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace ...`

PR-template checklist (`.github/PULL_REQUEST_TEMPLATE.md:52-56`):

- [ ] Notebook runs end-to-end without errors
- [ ] Results match expected output
- [ ] Visualization renders correctly
- [ ] Data connectors work with current API versions
- [ ] Documentation is clear and accurate

The January 2026 audit (`CHANGELOG.md:34-63`) is the nearest equivalent of a
test suite — an independent manual review that regraded every applied
econometrics notebook from B+/C+ up to A/A-. Criteria rediscovered at audit
time: methodology citations, sensitivity analyses, pre-programmed-effect
disclosures, data-provenance badges.

Contributions that define their own *numerical* checks inside cells (e.g.
"Validity Tests" H2 in NB15) function as embedded assertions — but they are
not collected, summarised, or gated by any external runner.

---

## 14. Deployment & Operations

### 14.1 Deployed Artefacts

| Artefact | Host | Mechanism |
|----------|------|-----------|
| Jekyll docs site | GitHub Pages (`khipuresearch.github.io/KASS/`) | `.github/workflows/pages.yml` on push to `main` |
| Rendered notebook HTMLs | Same (under `/KASS/demos/`) | Checked in at `docs/demos/*.html`; regenerated manually offline |
| Pricing page | Published at `bcdelodx.github.io/KASS/pricing.html` (per `README.md:183`) | Manual — checked-in root `pricing.html`; deployment path inconsistent with org URL |

### 14.2 Branching, Release, Rollback

Single long-lived `main` branch; no tags in recent log; monthly commit cadence;
no `CODEOWNERS`. Rollback is unformalised — `git revert` + re-run Pages
workflow, since every deployable artefact is static.

### 14.3 External Services

FRED API (6/6 notebooks); BLS API (NB07); Stripe Payment Links (placeholder
URLs in `CHANGELOG.md`); GitHub Pages; GitHub Actions (3 workflows).

---

## 15. Module Inventory

### 15.1 Python Modules

Exactly **one**:

- `fix_badges.py` (69 lines, root) — a single-purpose utility that rewrites
  the first markdown cell of each notebook, replacing shields.io-style badges
  with plain-text "KRL Suite v2.0 | Tier: X | Data: Y" strings so that the
  notebooks export cleanly to LaTeX. Hard-coded lookup table at lines 17-25
  maps notebook number → badge string. Iterates the six notebook paths at
  lines 8-15.

This is the only `.py` file in the repository. There are no packages, no
`__init__.py` files, no importable modules.

### 15.2 Notebooks (6 total)

Metadata harvested with `jq '.cells | length'` and `.metadata.kernelspec`.
Every notebook uses kernel `.venv-workspace` (`language: python`,
`name: python3`). All six begin with an identical KR-Labs branding cell
(cell 0, markdown, ~9 lines of HTML).

#### `notebooks/applied-econometrics/07-labor-market-intelligence.ipynb`

- Cells: 28 (16 markdown, 12 code)
- Size: 272 KB
- Tier: Community (`fix_badges.py:19`)
- Data: BLS + FRED
- H2 outline: KASS Notebook | Applied Econometrics Series → KRL Suite
  Components & Pricing → Motivation → Executive Summary → 1. Environment
  Setup → 2. Fetch Labor Market Data → 3. Metro-Level Labor Market Dataset
  → 4. Labor Market Health Visualization → 5. Skills Gap and Automation Risk
  Analysis → 6. Wage Compression Analysis → 7. Key Findings Summary →
  Limitations & Interpretation → References → Appendix: KRL Suite Components
  Used
- Audit grade: C+ → A- (`CHANGELOG.md:38`)
- Remediation: demo fallback removed, Bartik/Katz-Murphy/Autor citations
  added, 0.30–0.50 threshold sensitivity analysis, provenance badge
- Distinct imports: `krl_models.{LocationQuotient, ShiftShare, STLAnomaly}`,
  `sklearn.preprocessing.MinMaxScaler`, `scipy.stats.pearsonr`

#### `notebooks/applied-econometrics/20-opportunity-zone-evaluation.ipynb`

- Cells: 32 (18 markdown, 14 code)
- Size: 996 KB
- Tier: Professional (`fix_badges.py:20`)
- Data: FRED County Economics
- H2 outline: Series banner → KRL Suite Components & Pricing → ⚠️ HYBRID DATA
  STRUCTURE NOTICE → Motivation → 1. Environment Setup → 2. Fetch Real
  County Economic Data from FRED → Identification Strategy → 3. Selection
  Analysis → 4. Impact Estimation (DiD, Community Tier) → Pro Tier: Spatial
  Spillover Analysis → Enterprise Tier: Comprehensive OZ Evaluation →
  5. Executive Summary
- Audit grade: B+ → A (`CHANGELOG.md:58`)
- Remediation: hybrid-data disclosure, county-aggregation-bias warning,
  pre-programmed-effect documentation, provenance badge
- Distinct imports: `krl_enterprise.OpportunityZoneEvaluator`,
  `matplotlib.patches`, `sklearn.linear_model.LogisticRegression`

#### `notebooks/applied-econometrics/22-workforce-development-roi.ipynb`

- Cells: 32 (16 markdown, 16 code)
- Size: 211 KB
- Tier: Professional (`fix_badges.py:21`)
- Data: FRED Labor Market
- H2 outline: Series banner → KRL Suite Components & Pricing →
  ⚠️ METHODOLOGICAL DEMONSTRATION NOTICE → Motivation → 1. Environment Setup
  → 2. Fetch Labor Market Context from FRED → Identification Strategy →
  3. Impact Estimation (Community Tier) → 4. Cost-Benefit Analysis →
  Sensitivity Analysis → Enterprise Tier: WIOA-Compliant Reporting →
  5. Executive Summary
- Audit grade: B+ → A- (`CHANGELOG.md:47`)
- Remediation: methodological-demo warning, Cinelli-Hazlett (2020) omitted-
  variable-bias sensitivity, OMB-A-4/JobCorps/Card-et-al-2018 parameter
  citations, removed A+ self-cert, removed tier-marketing prose
- Distinct imports: `krl_enterprise.WorkforceROICalculator`,
  `sklearn.neighbors.NearestNeighbors`,
  `sklearn.linear_model.{Linear, Logistic}Regression`

#### `notebooks/causal-inference/11-heterogeneous-treatment-effects.ipynb`

- Cells: 32 (16 markdown, 16 code)
- Size: 1.77 MB (**largest notebook**)
- Tier: Pro + Enterprise (`fix_badges.py:22`)
- Data: FRED State Economics
- H2 outline: Series banner → KRL Suite Components & Pricing → Motivation →
  2. Fetch Real Employment Data from FRED → Identification Strategy →
  3. Community Tier: ATE Estimation → Pro Tier: Causal Forest for ITEs →
  4. Policy Targeting → Enterprise Tier: Double Machine Learning →
  🔍 Sensitivity Analysis: Robustness to Unmeasured Confounding →
  5. Key Findings & Recommendations → External Validity
- Distinct imports: `krl_policy.enterprise.DoubleML`,
  `sklearn.ensemble.{RandomForest, GradientBoosting}Regressor`,
  `sklearn.model_selection.cross_val_predict`
- Notes: includes embedded HTML/image payloads → explains the size

#### `notebooks/causal-inference/14-synthetic-control-policy-lab.ipynb`

- Cells: 26 (14 markdown, 12 code)
- Size: 250 KB
- Tier: Community (`fix_badges.py:23`)
- Data: FRED State Economics
- H2 outline: Series banner → KRL Suite Components & Pricing → Motivation →
  2. Fetch Real State-Level Unemployment Data → 3. Visualize the Policy
  Evaluation Problem → Identification Strategy → 4. Community Tier: Basic
  Synthetic Control → Pro Tier: Donor Pool Selection & Placebo Inference →
  Enterprise Tier: Multi-Unit Synthetic Control → Robustness Checks &
  Placebo Tests → Limitations & Interpretation → 5. Executive Summary
- Distinct imports: `krl_causal_policy.enterprise.MultiUnitSCM`,
  `scipy.optimize`, `scipy.stats.linregress`
- Carries the canonical environment-bootstrap logic (`KRL_DEV_PATH`) copied
  across all notebooks

#### `notebooks/causal-inference/15-regression-discontinuity-toolkit.ipynb`

- Cells: 26 (13 markdown, 13 code)
- Size: 301 KB
- Tier: Community (`fix_badges.py:24`)
- Data: FRED County Economics
- H2 outline: Series banner (ordinal "15") → KRL Suite Components & Pricing
  → Motivation → Data → Identification Strategy → 3. Community Tier: Basic
  Sharp RDD → Pro Tier: Optimal Bandwidth Selection → Enterprise Tier:
  Advanced RDD Extensions → Validity Tests → Limitations & Interpretation →
  5. Executive Summary → References
- Distinct imports: `krl_causal_policy.enterprise.{MulticutoffRDD, RDKink}`,
  `sklearn.preprocessing.PolynomialFeatures`,
  `sklearn.linear_model.LinearRegression`

### 15.3 Documentation Modules (`docs/`)

| File | Lines | Front-matter nav_order |
|------|-------|------------------------|
| `docs/index.md` | 62 | 1 (Home) |
| `docs/getting-started.md` | 48 | 2 |
| `docs/methodology.md` | 69 | 4 |
| `docs/about.md` | 56 | 5 |
| `docs/notebooks/index.md` | 33 | (nav_order 3 implied) |
| `docs/notebooks/heterogeneous-treatment-effects.md` | 55 | — |
| `docs/notebooks/synthetic-control.md` | 56 | — |
| `docs/notebooks/regression-discontinuity.md` | 61 | — |
| `docs/notebooks/labor-market-intelligence.md` | 60 | — |
| `docs/notebooks/opportunity-zone-evaluation.md` | 60 | — |
| `docs/notebooks/workforce-development-roi.md` | 62 | — |

### 15.4 Governance / Process Artefacts

Root: `CHANGELOG.md` (87), `CONTRIBUTING.md` (481), `LICENSE` (201, Apache 2.0),
`README.md` (332). `.github/`: `SECURITY.md` (102), `CODE_OF_CONDUCT.md`,
`PULL_REQUEST_TEMPLATE.md` (75), `FUNDING.yml` (15),
`ISSUE_TEMPLATE/{bug_report,config,data_connector,documentation,feature_request,notebook_improvement}.yml`.

### 15.5 Internal Staging (gitignored, present in working tree)

`KASS_NOTEBOOK_PRACTICAL_WORKFLOW.md` (1,273), `KASS_NOTEBOOK_UPDATE_DIRECTIVE.md`
(1,446), `KASS_Discussion_Labels/`, `KASS_Issues/`, `KASS_Pull_Template/` — each
staging dir carries its own shell deploy script. `.gitignore:60-65` flags
these as "Internal staging files (already deployed to .github/)".

---

## 16. Known Gaps & Risks

### 16.1 Missing `requirements.txt`

Both `README.md:38` and `docs/getting-started.md:28-30` instruct users to run
`pip install -r requirements.txt`, but the file does not exist. Every
first-time clone will fail at this step. PR checklist item
(`PULL_REQUEST_TEMPLATE.md:69`) references a file the repo has never had.

### 16.2 KRL Suite Is Not Publicly Installable

All six notebooks import `krl_core`, `krl_data_connectors`, plus one or more
of `krl_models`, `krl_policy`, `krl_causal_policy`, `krl_enterprise`. None of
these is on public PyPI. Without `KRL_DEV_PATH` pointing to a private
checkout, the notebooks will not run end-to-end. The "Quick Start" promise
(`README.md:33-40`) is only deliverable to users with platform credentials —
a significant gap for a repository positioned as open-source educational
content.

### 16.3 Rendered Demos May Drift from Source

`notebook_results/*.html` timestamps (Jan 8, 2026) predate the Feb 13
"notebook updates" commit. There is no CI to re-render; regeneration is
manual. Users visiting the hosted demos may view stale outputs without
warning.

### 16.4 Demo Fallback Removal Is One-Directional

Post-audit (`CHANGELOG.md:40`), NB07 now raises `RuntimeError` if API keys
are absent. Because there is no test harness, regressions that accidentally
re-introduce fallback mock data would pass review. The audit grade is a
point-in-time snapshot, not a standing gate.

### 16.5 Pricing URL Inconsistency

`README.md:183` links to `bcdelodx.github.io/KASS/pricing.html` (personal
account), while `docs/_config.yml:5` and `README.md:16` use
`khipuresearch.github.io/KASS/` (organisation). The pricing page is not
linked from the Jekyll site at all. Stripe links in `CHANGELOG.md:13-17`
are explicitly placeholders (`https://buy.stripe.com/krl_pro_monthly` etc.).

### 16.6 Hybrid Data + Pre-Programmed Effects

NB20 and NB22 mix real FRED pulls with simulated treatment effects
(`CHANGELOG.md:47-63`). The audit added prominent warnings, but the
signal-to-noise ratio is low enough that external readers could mistake
illustrative magnitudes for estimated impacts. This is flagged as a
remediated concern, not an eliminated one.

### 16.7 No Dependency Security Scanning

`SECURITY.md:62` instructs users to run `pip-audit` themselves. No SBOM,
Dependabot, Renovate, or GitHub Advanced Security is configured on this repo
(no dependency file for them to scan, admittedly). A vulnerable pinned
version in a future notebook contribution would go undetected by repo-level
automation.

### 16.8 Documentation vs Reality Drift

Examples of in-repo documentation making claims that the repo itself does
not back:

- "125+ causal inference models" (`README.md:145`, `docs/about.md:13`) —
  none shipped here; all proprietary.
- "68+ authoritative data sources" (`README.md:143`, `docs/about.md:12`) —
  two API wrappers (FRED, BLS) are reachable from the notebooks.
- `CONTRIBUTING.md:37` lists `statsmodels`, `econml`, `causalml` as "core
  dependencies" — none of these appears in a single notebook import.

These aren't bugs; they're marketing-vs-engineering delta that a forensic
reader should be aware of when evaluating the repository against its own
positioning.

### 16.9 Single-Branch, No CODEOWNERS

There is no `CODEOWNERS`, no branch protection evidence, no required-review
rules in tree. Governance is cultural rather than enforced.

### 16.10 Empty Placeholders

`data/` and `docs/assets/images/` are both empty directories. They are
checked in as shape-only scaffolding, serving as an implicit contract for
future content that is not yet present.

---

## Appendix A — Evidence Index

Primary sources read in full: `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`,
`.github/SECURITY.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/FUNDING.yml`,
`.github/workflows/{pages,issue-management,stale}.yml`, `.gitignore`,
`docs/_config.yml`, `docs/Gemfile`, `docs/{index,getting-started,methodology,about}.md`,
`fix_badges.py`. Notebook metadata via `jq '.cells | length'`,
`'.metadata.kernelspec'`, and markdown/code-cell source extraction.

---

*End of SPEC — KASS. Generated 2026-04-23 against commit
`27061e8a2d9b18bc1c2b6d06d0bf1deb3918bb19` on `main`.*
