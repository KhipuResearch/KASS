# ARCHITECTURE — KASS

> Companion to [`SPEC.md`](SPEC.md). This file describes the topology of the
> **demonstration platform** as it exists in-repo. Most sub-sections below are
> marked **Not applicable** because KASS is neither a service nor a package;
> each *Not applicable* carries a one-line justification that traces back to
> SPEC evidence.

---

## 1. System Shape (One-Paragraph Summary)

KASS is a **content repository with a static-site build pipeline**. Six
Jupyter notebooks live under `notebooks/`; they import a private `krl_*`
suite (not in-tree) and pull live FRED/BLS data at execution time. The six
notebooks are **manually** rendered to HTML (via `nbconvert`, off-CI) into
`notebook_results/` and `docs/demos/`. A Jekyll site under `docs/` — built
by `.github/workflows/pages.yml` on push to `main` — publishes the narrative
pages plus those pre-rendered HTML files to GitHub Pages. There is no
backend, no API, no daemon, no database. Everything deployable is static.

```
┌─────────────────────────┐         ┌──────────────────────────┐
│ notebooks/*.ipynb       │──(jq/   │ notebook_results/*.html  │
│  · 6 files, kernel       │   nb   │  (manual nbconvert,      │
│    .venv-workspace      │ convert)│   off-CI)                │
│  · imports krl_* suite   │────────▶│                          │
│    (external, private)   │         └──────────┬──────────────┘
└──────────┬───────────────┘                    │ copy/commit
           │ depends on (at run time)           ▼
           │                           ┌──────────────────────────┐
           ▼                           │ docs/                    │
┌─────────────────────────┐            │  · _config.yml (baseurl  │
│ FRED / BLS public APIs  │            │    /KASS)                │
│  via krl_data_connectors│            │  · just-the-docs theme   │
│  (FRED_API_KEY,         │            │  · demos/*.html          │
│   BLS_API_KEY via       │            │  · notebooks/*.md        │
│   python-dotenv)        │            └──────────┬───────────────┘
└─────────────────────────┘                       │
                                                  │  .github/workflows/pages.yml
                                                  ▼
                                       ┌──────────────────────────┐
                                       │ GitHub Pages             │
                                       │  khipuresearch.github.io │
                                       │    /KASS/                │
                                       └──────────────────────────┘
```

---

## 2. Content Topology

| Layer | Location | Purpose | Source of truth |
|-------|----------|---------|-----------------|
| Notebooks | `notebooks/applied-econometrics/`, `notebooks/causal-inference/` | Executable analytical content | `SPEC.md §3.1, §15.2` |
| Pre-rendered HTML | `notebook_results/*.html` | Canonical pre-executed outputs (6 files, ~4.5 MB total) | `SPEC.md §5, §9.3` |
| Demo mirrors | `docs/demos/*.html` | Copies published by Jekyll | `SPEC.md §5, §14.1` |
| Jekyll pages | `docs/{index,about,getting-started,methodology}.md`, `docs/notebooks/*.md` | Narrative documentation | `SPEC.md §15.3` |
| Jekyll config | `docs/_config.yml`, `docs/Gemfile`, `docs/_sass/**` | Theme + build config | `SPEC.md §7.1, §7.2` |
| Governance | `CONTRIBUTING.md`, `.github/SECURITY.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/ISSUE_TEMPLATE/*`, `CODE_OF_CONDUCT.md`, `LICENSE` | Policy / process | `SPEC.md §15.4` |
| CI | `.github/workflows/{pages,issue-management,stale}.yml` | GitHub Pages deploy + repo hygiene | `SPEC.md §6.4, §7.3, §7.4` |
| Staging (gitignored) | `KASS_Issues/`, `KASS_Discussion_Labels/`, `KASS_Pull_Template/`, `KASS_NOTEBOOK_*.md` | Migration scaffolding | `SPEC.md §5, §15.5` |
| Standalone artefacts | `pricing.html` (root), `fix_badges.py`, `LICENSE`, `CHANGELOG.md` | Out-of-tree referenced assets | `SPEC.md §15.1, §14.1` |

---

## 3. Notebook-Rendering Pipeline

The rendering pipeline is **manual**. There is no `.github/workflows/*.yml`
that runs `jupyter nbconvert`; `SPEC.md §6.5` confirms this and flags it as
a drift risk.

Steps, as practised per `CONTRIBUTING.md:270-272` and `SPEC.md §6.5`:

1. Author edits `notebooks/<domain>/<N>-<slug>.ipynb` locally.
2. Author executes the notebook against a local KRL environment
   (`KRL_DEV_PATH` set, `.env` present with `FRED_API_KEY` / `BLS_API_KEY`).
3. Author formats with `black <notebook>.ipynb`.
4. Author runs `jupyter nbconvert --ClearOutputPreprocessor.enabled=True
   --inplace <notebook>.ipynb` before commit (for clean diffs).
5. Author separately runs `jupyter nbconvert --to html <notebook>.ipynb`
   and copies the output into both `notebook_results/` and `docs/demos/`.
6. `git push origin main` triggers `.github/workflows/pages.yml`, which
   builds Jekyll and publishes the HTML verbatim to GitHub Pages.

Drift surface: steps 5 and 2 are decoupled in time, so the Pages site can
serve HTML rendered from an older notebook-source commit (`SPEC.md §16.3`).

---

## 4. Build & Deploy Pipeline (the only CI path that exists)

| Stage | Runner | Evidence |
|-------|--------|----------|
| Jekyll build | `ubuntu-latest`, Ruby 3.2, `bundle install && bundle exec jekyll build --baseurl /KASS` | `.github/workflows/pages.yml:17-43` |
| Artifact upload | `actions/upload-pages-artifact@v3` | `.github/workflows/pages.yml:45-48` |
| Deploy | `actions/deploy-pages@v4` into `github-pages` environment | `.github/workflows/pages.yml:50-59` |
| Concurrency | `group: pages, cancel-in-progress: false` | `.github/workflows/pages.yml:13-15` |
| Trigger | `push` to `main` or `workflow_dispatch` | `.github/workflows/pages.yml:3-6` |

No `Gemfile.lock` is committed; the Jekyll build relies on the CI runner to
resolve Gem versions from `docs/Gemfile` (`SPEC.md §6.4`, commit
`4f8def8`).

---

## 5. Data Flow

**Not applicable as an in-repo concern.** The repository stores no data
(`data/` is empty, `.gitignore:31-37` excludes all tabular file types;
`SPEC.md §9.1`). At notebook-execution time, each notebook calls FRED via
`krl_data_connectors.professional.{fred_full.FREDFullConnector,
FREDFullConnector}` (and NB07 additionally calls BLS via
`krl_data_connectors.community.*`). The network surface belongs to those
third-party APIs; the repo itself merely holds the calling code.

---

## 6. Authentication / Authorization Topology

**Not applicable at the repository level.** `SPEC.md §10` records that all
auth logic lives inside the proprietary `krl_*` libraries; KASS has no
users, sessions, tokens, or ACLs of its own. The only secret surface is the
two environment variables (`FRED_API_KEY`, `BLS_API_KEY`) loaded by
`python-dotenv` at notebook start — documented in
[`policy/secrets.yaml`](policy/secrets.yaml).

---

## 7. Observability Topology

**Not applicable.** Per `SPEC.md §12`, there is no service to observe. The
notebooks emit logs through `krl_core.get_logger` — a proprietary wrapper
whose behaviour is defined outside this repository. No metrics, traces, or
error-reporting integrations ship here.

---

## 8. Service-to-Service / Internal Communication

**Not applicable.** There are no services. The "internal" link surface is
a single Jekyll site linking to six static HTML files plus a root
`pricing.html`. See [`DECISIONS/0003-pricing-url-conflict.md`](DECISIONS/0003-pricing-url-conflict.md)
for the unresolved host mismatch between those links.

---

## 9. External-Service Surface

Three categories, all consumed read-only by notebooks or Jekyll:

| Service | Consumed by | Evidence |
|---------|-------------|----------|
| FRED public REST API | All 6 notebooks (`krl_data_connectors`) | `SPEC.md §4, §14.3` |
| BLS public REST API | NB07 (`krl_data_connectors.community.*`) | `SPEC.md §4.NB07` |
| GitHub Pages | Jekyll deploy target | `.github/workflows/pages.yml` |
| GitHub Actions | 3 workflows (pages, issue-management, stale) | `SPEC.md §14.3, §7.3, §7.4` |
| Stripe Payment Links | Documented in `CHANGELOG.md:13-17`; **placeholder URLs** | `SPEC.md §8, §14.3, §16.5` |

Inbound traffic: **zero**. KASS does not host any listener.

---

## 10. Failure Modes & Graceful Degradation

Per `CHANGELOG.md:3-30` and `SPEC.md §10`, the notebooks implement a
tier-aware graceful-degradation pattern: when a Community-tier user imports
a Pro or Enterprise feature from the `krl_*` suite, the notebook displays an
upgrade banner with Stripe links and falls back to a lower-tier equivalent
(e.g. `FREDBasicConnector` in place of `FREDFullConnector`). This is
implemented inside the proprietary `krl_*` libraries, not in this
repository — the repo only demonstrates the user-visible behaviour.

Post-audit, NB07 no longer degrades if `FRED_API_KEY` / `BLS_API_KEY` are
absent: it raises `RuntimeError` (`CHANGELOG.md:40`, `SPEC.md §16.4`). No
automated test guards this behaviour.

---

## 11. Scaling & Performance

**Not applicable.** There is no runtime component to scale. GitHub Pages
absorbs read traffic; notebook execution happens on the end-user's machine.
The largest single artefact in the repository is
`notebooks/causal-inference/11-heterogeneous-treatment-effects.ipynb` at
1.77 MB (`SPEC.md §15.2.NB11`), driven by embedded plot payloads.

---

## 12. Known Architectural Risks

Tracked in `SPEC.md §16` and in [`CALIBRATION_REQUIRED.md`](CALIBRATION_REQUIRED.md).
The three most consequential are captured as formal ADRs:

| ADR | Risk |
|-----|------|
| [`0001-demo-only-no-proprietary-compute`](DECISIONS/0001-demo-only-no-proprietary-compute.md) | Repo is a funnel, not self-contained; external users cannot run notebooks. |
| [`0002-missing-requirements-txt-gap`](DECISIONS/0002-missing-requirements-txt-gap.md) | Quick-start instruction references a file that does not exist. |
| [`0003-pricing-url-conflict`](DECISIONS/0003-pricing-url-conflict.md) | README and `_config.yml` disagree on the canonical host. |

Additional unremediated risks (dependency scanning, rendered-demo drift,
`CODEOWNERS`, documentation-vs-reality deltas) are recorded in the
calibration document.

---

*End of ARCHITECTURE — KASS.*
