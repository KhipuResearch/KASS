# CALIBRATION_REQUIRED — KASS

> Every `<TOKEN_TBD::...>` placeholder in the control-artefact stack is
> catalogued here. This document is the single reconciliation target: every
> token below must be resolved before the demo repository can be described
> as "calibrated." Resolution is *not* a prerequisite for the stack to be
> useful — the artefacts are operationally complete in their current
> advisory state — but an uncalibrated repository accumulates unresolved
> decisions that eventually block real work.
>
> **How to resolve a token:** edit the owning file, replace the
> `<TOKEN_TBD::...>` with a concrete value, remove the row from the table
> below, and (if the change is non-trivial) cite or author an ADR.

Generated: 2026-04-23. Source of truth: [`SPEC.md`](SPEC.md).

---

## 1. Calibration Inventory

### 1.1 From `policy/access-control.yaml`

| Token | Decision required | Default / interim stance |
|-------|-------------------|--------------------------|
| `<TOKEN_TBD::required-reviews-count>` | How many reviews does a PR to `main` require? | Operate as "≥1 maintainer" until set. |
| `<TOKEN_TBD::dismiss-stale-reviews>` | Dismiss approvals when new commits land? | Conservative: yes. |
| `<TOKEN_TBD::enforce-branch-protection-on-admins>` | Does branch protection bind admins? | Recommended: yes. |
| `<TOKEN_TBD::restrict-direct-push-to-main>` | Forbid direct push? | Recommended: yes. |
| `<TOKEN_TBD::require-linear-history>` | Require rebase/squash merges? | No stance today. |
| `<TOKEN_TBD::maintainer-members-list>` | Explicit list of GitHub usernames. | KRL engineering team (implicit). |
| `<TOKEN_TBD::security-responder-members-list>` | Who triages `security@krlabs.dev`? | Implicit: SECURITY.md-listed. |
| `<TOKEN_TBD::pr-required-approvals>` | Numeric count (duplicates above intentionally — different field in spec). | — |
| `<TOKEN_TBD::github-apps-allowlist>` | Which GitHub Apps may install. | None until decided. |

### 1.2 From `policy/secrets.yaml`

| Token | Decision required |
|-------|-------------------|
| `<TOKEN_TBD::fred-key-rotation-owner>` | Named individual or role. |
| `<TOKEN_TBD::fred-key-rotation-cadence>` | e.g. every 90 days. |
| `<TOKEN_TBD::bls-key-rotation-owner>` | Named individual or role. |
| `<TOKEN_TBD::bls-key-rotation-cadence>` | e.g. every 90 days. |
| `<TOKEN_TBD::ship-dot-env-example>` | Commit a `.env.example` with empty placeholder values. |
| `<TOKEN_TBD::baseline-rotation-cadence>` | Default cadence for any future key. |
| `<TOKEN_TBD::secret-scanner-tool>` | gitleaks, trufflehog, or GAS. |

### 1.3 From `policy/dependency.yaml`

| Token | Decision required |
|-------|-------------------|
| `<TOKEN_TBD::ship-requirements-txt>` | Supersede ADR-0002 by committing the file. |
| `<TOKEN_TBD::requirements-txt-owner>` | Who maintains it once it exists. |
| `<TOKEN_TBD::python-maximum-version>` | Upper bound on supported Python. |
| `<TOKEN_TBD::pandas-min>` through `<TOKEN_TBD::plotly-min>` | Version pins (9 packages). |
| `<TOKEN_TBD::jupyter-min>`, `<TOKEN_TBD::jupyterlab-min>` | Runtime version pins. |
| `<TOKEN_TBD::statsmodels-adopt-or-remove>` | Adopt in a notebook *or* remove from CONTRIBUTING.md:37. |
| `<TOKEN_TBD::econml-adopt-or-remove>` | Same. |
| `<TOKEN_TBD::causalml-adopt-or-remove>` | Same. |
| `<TOKEN_TBD::enable-dependabot>` | Boolean. |
| `<TOKEN_TBD::enable-renovate>` | Boolean. |
| `<TOKEN_TBD::enable-codeql>` | Boolean. |
| `<TOKEN_TBD::sbom-format>` | CycloneDX, SPDX, or none. |
| `<TOKEN_TBD::req-txt-pin-strategy>` | floor-only / floor-ceiling / exact-pin. |

### 1.4 From `policy/ci-authority.yaml`

| Token | Decision required |
|-------|-------------------|
| `<TOKEN_TBD::wire-test-workflow>` | Wire or defer the tests workflow. |
| `<TOKEN_TBD::wire-nbconvert-workflow>` | Automate notebook rendering. |
| `<TOKEN_TBD::wire-link-check-workflow>` | Automate outbound-link validation. |
| `<TOKEN_TBD::wire-pip-audit-workflow>` | Automate dependency audit. |
| `<TOKEN_TBD::wire-secret-scan-workflow>` | Automate secret scanning. |
| `<TOKEN_TBD::wire-notebook-diff-guard>` | Guard against dirty-output commits. |
| `<TOKEN_TBD::pin-actions-to-sha>` | Pin GH Action dependencies by SHA. |
| `<TOKEN_TBD::top-level-timeout-minutes>` | Default workflow timeout. |
| `<TOKEN_TBD::pages-env-protection-rules>` | Protection rules on the `github-pages` environment. |
| `<TOKEN_TBD::versioning-scheme>` | Tags, semver, calver, or none. |
| `<TOKEN_TBD::release-workflow-or-none>` | Introduce a release workflow or stay release-less. |

### 1.5 From `DECISIONS/0001-demo-only-no-proprietary-compute.md`

| Token | Decision required |
|-------|-------------------|
| `<TOKEN_TBD::krl-oss-namespace-strategy>` | Shared vs distinct namespaces for a future public-minimal variant. |
| `<TOKEN_TBD::rendered-demo-freshness-SLA>` | How fresh must `notebook_results/*.html` be? |
| `<TOKEN_TBD::license-notice-for-krl-runtime>` | Add an explicit notice clarifying the proprietary runtime. |

### 1.6 From `DECISIONS/0002-missing-requirements-txt-gap.md`

| Token | Decision required |
|-------|-------------------|
| `<TOKEN_TBD::req-txt-pin-strategy>` | (duplicate of 1.3 — same decision.) |
| `<TOKEN_TBD::req-dev-split-strategy>` | Single file or split dev dependencies. |
| `<TOKEN_TBD::krl-suite-in-requirements-strategy>` | Include `krl_*` as best-effort entries or omit. |

### 1.7 From `DECISIONS/0003-pricing-url-conflict.md`

| Token | Decision required |
|-------|-------------------|
| `<TOKEN_TBD::pricing-host-canonicalisation>` | Alternative 3.1 (docs/) vs 3.2 (external). |
| `<TOKEN_TBD::external-pricing-host-URL>` | If 3.2 chosen: the URL. |
| `<TOKEN_TBD::bcdelodx-host-deprecation-owner>` | Who retires the personal-account host. |
| `<TOKEN_TBD::stripe-payment-link-surface>` | Secret vs CHANGELOG vs KRL runtime vs page only. |

### 1.8 From `tests/README.md`

| Token | Decision required |
|-------|-------------------|
| `<TOKEN_TBD::test-coverage-floor>` | 80% is the project-wide standard; does KASS match? |
| `<TOKEN_TBD::test-runner-choice>` | `pytest` expected but not formally chosen. |
| `<TOKEN_TBD::e2e-tests-gate-on-krl-dev-path>` | Policy for skipping e2e/ when `KRL_DEV_PATH` unset. |

---

## 2. Risks Not Yet Token-Tracked

Residual `SPEC.md §16` risks that are not currently fronted by a specific
token because they require upstream decisions first:

- **§16.3 Rendered Demos May Drift from Source.** Fully surfaces once
  `<TOKEN_TBD::wire-nbconvert-workflow>` is decided.
- **§16.6 Hybrid Data + Pre-Programmed Effects (NB20, NB22).** Remediated
  via the January 2026 audit (`CHANGELOG.md:47-63`) but not structurally
  prevented from regressing. A potential future CALIBRATION entry:
  `<TOKEN_TBD::hybrid-data-disclosure-linter>`.
- **§16.8 Documentation vs Reality Drift ("125+ causal inference models",
  "68+ authoritative data sources").** Marketing claims live in
  `README.md` and `docs/about.md`; neither ADR-0001 nor ADR-0002 removes
  them. A potential future CALIBRATION entry:
  `<TOKEN_TBD::marketing-claim-substantiation-or-removal>`.
- **§16.9 Single-Branch, No CODEOWNERS.** Partially addressed in
  `policy/access-control.yaml` through the `maintainer-members-list`
  token; a full fix would materialise as a `CODEOWNERS` file. Potential
  future CALIBRATION entry: `<TOKEN_TBD::ship-codeowners-file>`.
- **§16.10 Empty Placeholders** (`data/`, `docs/assets/images/`). No
  owner today. Potential future CALIBRATION entry:
  `<TOKEN_TBD::empty-placeholder-disposition>`.

---

## 3. Resolution Workflow

1. Pick a token. Open its owning file plus any cross-referencing files
   (grep for the token string first).
2. Write an ADR in `DECISIONS/` if the decision is non-trivial or
   cross-cutting. Use the next available number
   (`DECISIONS/0004-...`; see `policy/access-control.yaml`
   `decisions_directory.next_number`).
3. Replace the `<TOKEN_TBD::...>` with the chosen value in every file
   that references it.
4. Delete the resolved row from §1 of this document.
5. Open a PR. Follow
   [`policy/access-control.yaml`](policy/access-control.yaml)
   `review_requirements.policy_changes`.

---

## 4. Related Artefacts

- [`SPEC.md`](SPEC.md) — forensic reality.
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — topology map; §12 cross-links the
  three ADRs.
- [`DECISIONS/`](DECISIONS/) — ADRs 0001–0003.
- [`policy/`](policy/) — four policy YAMLs (access, secrets, dependency,
  CI authority).
- [`tests/README.md`](tests/README.md) — why the test suite is absent and
  how to start one.
- [`.github/workflows/README.md`](.github/workflows/README.md) — CI
  present and absent.
