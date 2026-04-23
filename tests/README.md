# tests/

> **Status: Not applicable — no automated test suite ships in this repository.**

This directory exists to reserve a path for a future suite and to document
the remediation route. It is intentionally otherwise empty.

---

## 1. Current State

Per `SPEC.md §13`, KASS ships **zero** automated tests. Verified absences:

- No `tests/` subtree with `test_*.py` or `*_test.py` files.
- No `pytest.ini`, `tox.ini`, `conftest.py`, `noxfile.py`, `setup.cfg`
  `[tool:pytest]` section.
- No `.github/workflows/*.yml` that runs a test command. The three
  workflows present (`pages.yml`, `issue-management.yml`, `stale.yml`)
  are deploy/hygiene automation only. See
  [`.github/workflows/README.md`](../.github/workflows/README.md).
- `fix_badges.py` (root) is a one-shot migration script, not a test —
  `SPEC.md §15.1`.

The only quality discipline the repository exercises is **manual
end-to-end notebook execution** before merge. This is codified in
`CONTRIBUTING.md:270-272` (format with `black`, clear outputs with
`nbconvert --ClearOutputPreprocessor.enabled=True --inplace`) and in
`.github/PULL_REQUEST_TEMPLATE.md:52-56`:

- "Notebook runs end-to-end without errors"
- "Results match expected output"
- "Visualization renders correctly"
- "Data connectors work with current API versions"
- "Documentation is clear and accurate"

The January 2026 audit (`CHANGELOG.md:34-63`) is the nearest equivalent
of a test suite that has ever run against this repository — a point-in-
time independent review. `SPEC.md §13, §16.4` flag that the audit is a
snapshot, not a standing gate.

## 2. Why the gap is structural, not stylistic

Writing a conventional test suite for KASS runs into the same obstacle as
the Quick Start: every notebook depends on the private `krl_*` suite
(see [`DECISIONS/0001-demo-only-no-proprietary-compute.md`](../DECISIONS/0001-demo-only-no-proprietary-compute.md)).
Tests that exercise the notebooks end-to-end require `KRL_DEV_PATH` to
point at a private workspace or PyPI access to packages that do not exist
publicly. Tests that exercise individual cells in isolation require the
notebooks to be factored into importable modules — which
`SPEC.md §15.1` confirms they are not (the only `.py` file in the repo is
`fix_badges.py`).

A test suite is therefore not just unwritten; it is **blocked** on
decisions made in ADR-0001 (demo-only posture) and ADR-0002 (missing
`requirements.txt`).

## 3. Remediation Path

A realistic remediation sequence, in priority order:

1. **Smoke tests for notebook *syntax* and cell structure.** Does not
   require `krl_*`. Scope: import the notebook JSON via `nbformat`,
   assert cell counts match `SPEC.md §15.2` expectations, assert the
   first cell is the standard KR-Labs branding markdown, assert `jq`-
   queryable kernelspec is `.venv-workspace`. Runnable from plain PyPI.
2. **Static checks on the notebook Python source.** Extract all code
   cells to a temporary `.py` file and run `black --check`, `ruff
   check`, and `python -m py_compile` on it. Enforces
   `CONTRIBUTING.md:191-193, 270` automatically instead of on trust.
3. **Outbound-link validation.** Walk every Markdown file (including
   notebooks' markdown cells) and assert every URL responds 2xx. Would
   catch the conflict recorded in
   [`DECISIONS/0003-pricing-url-conflict.md`](../DECISIONS/0003-pricing-url-conflict.md)
   and the placeholder Stripe URLs in `CHANGELOG.md:13-17`.
4. **End-to-end notebook execution.** Only feasible once ADR-0001 is
   revisited. Requires either (a) a `krl-oss` public-only variant, or
   (b) CI-available secrets plus a private package index.
5. **Rendered-demo freshness check.** Compare mtime of each
   `notebooks/**/*.ipynb` against `notebook_results/*.html` and
   `docs/demos/*.html`; fail CI when notebook source is newer than
   rendered output. Addresses `SPEC.md §16.3`.

Items 1, 2, 3, and 5 are all achievable without touching ADR-0001.

## 4. Expected Structure (when this suite exists)

```
tests/
├── README.md                  (this file — remove "Not applicable" status)
├── conftest.py                (pytest fixtures; nbformat parsing)
├── smoke/
│   ├── test_notebook_structure.py
│   ├── test_kernelspec.py
│   └── test_branding_cell.py
├── lint/
│   ├── test_black_compliance.py
│   └── test_ruff_clean.py
├── links/
│   └── test_outbound_urls.py
├── freshness/
│   └── test_rendered_demos_current.py
└── e2e/                       (gated on KRL_DEV_PATH — skip when unset)
    ├── test_nb07_runs.py
    ├── test_nb11_runs.py
    ├── test_nb14_runs.py
    ├── test_nb15_runs.py
    ├── test_nb20_runs.py
    └── test_nb22_runs.py
```

Coverage target: `<TOKEN_TBD::test-coverage-floor>`. Runner:
`<TOKEN_TBD::test-runner-choice>` (`pytest` is the expected selection
but has not been formally chosen). CI wiring: track in
[`policy/ci-authority.yaml`](../policy/ci-authority.yaml) under
`workflows_absent_but_referenced.tests`.

## 5. Related Artefacts

- [`SPEC.md §13`](../SPEC.md) — forensic record of the gap.
- [`DECISIONS/0001-demo-only-no-proprietary-compute.md`](../DECISIONS/0001-demo-only-no-proprietary-compute.md)
  — why end-to-end tests are blocked.
- [`DECISIONS/0002-missing-requirements-txt-gap.md`](../DECISIONS/0002-missing-requirements-txt-gap.md)
  — why even lint-only tests need a manifest first.
- [`policy/ci-authority.yaml`](../policy/ci-authority.yaml) —
  `workflows_absent_but_referenced.tests` entry and calibration token.
- [`.github/workflows/README.md`](../.github/workflows/README.md) —
  current CI topology.
- [`CALIBRATION_REQUIRED.md`](../CALIBRATION_REQUIRED.md) — pending
  decisions gating this remediation.

## 6. Calibration Tokens Owned by This Document

- `<TOKEN_TBD::test-coverage-floor>`
- `<TOKEN_TBD::test-runner-choice>`
- `<TOKEN_TBD::e2e-tests-gate-on-krl-dev-path>` — policy for skipping the
  `e2e/` tier when `KRL_DEV_PATH` is unset in CI.
