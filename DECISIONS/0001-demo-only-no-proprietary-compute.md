# ADR-0001: Demo-only; no proprietary compute shipped in-repo

- **Status:** Accepted (documenting present reality)
- **Date:** 2026-04-23
- **Deciders:** Khipu Research Labs engineering (via repository evidence)
- **Supersedes:** n/a
- **Superseded by:** n/a

---

## 1. Context

KASS is positioned as an *open-source demonstration* of KRL's causal-inference
and policy-analysis methods (`README.md:3`, `SPEC.md §1`). The repository
contains six Jupyter notebooks plus a Jekyll documentation site. The notebooks
themselves, however, import six private packages — `krl_core`,
`krl_data_connectors`, `krl_models`, `krl_policy`, `krl_enterprise`,
`krl_causal_policy` (`SPEC.md §3.4`). Those packages are **not** vendored in
this repository, **not** on public PyPI, and **not** installable without KRL
platform credentials or a local checkout of the private `Private IP/`
workspace pointed to by `KRL_DEV_PATH` (`SPEC.md §3.4`, notebook bootstrap
cell).

The practical consequence (`SPEC.md §16.2`): an external reader who clones
the repository and follows the Quick Start cannot execute a single notebook
end-to-end. They can read the source, they can view pre-rendered HTML at
`https://khipuresearch.github.io/KASS/demos/*.html`, but they cannot run the
analyses. This matters because the repository is marketed as
"open-source . . . production-grade" (`README.md:3`) and as "A learning
resource for applied researchers" (`README.md:52`).

## 2. Decision

KASS is explicitly structured as a **marketing and documentation funnel** for
the proprietary KRL platform, *not* as a self-contained open-source package.
Every notebook depends on private KRL suite modules; every notebook ends
with a "KRL Suite Components & Pricing" section (`SPEC.md §1`); the hosted
pricing page and Stripe Payment Links are first-class artefacts
(`CHANGELOG.md:7-20`, `pricing.html`). The decision to keep proprietary
compute **out** of this repository — and therefore to accept that external
users cannot run the notebooks — is intentional. The Apache-2.0 licence
covers the *source text* of the notebooks and the accompanying
documentation, not the execution path through `krl_*`.

Architectural commitments that follow from this decision:

1. No attempt is made to stub, mock, or vendor the `krl_*` packages.
2. No attempt is made to provide a synthetic-data fallback inside the
   notebooks — the January 2026 audit removed the NB07 fallback precisely
   because it obscured the real data dependency (`CHANGELOG.md:40`).
3. The Quick Start remains a *KRL-team* Quick Start; the public-user Quick
   Start is "view the rendered HTML."

## 3. Alternatives Considered

### 3.1 Vendor a public-only minimal variant of `krl_*`

Extract a subset of `krl_core` (logger, config) and
`krl_data_connectors` (FRED/BLS community connectors) into a small
`krl-oss` package on PyPI, sufficient for at least the three Community-tier
notebooks (NB07, NB14, NB15) to run.

- **Pro:** Honours the "open-source" framing. External learners can execute
  the methodology notebooks.
- **Con:** Creates a second package to maintain; requires a careful split
  between open and closed capabilities; increases the surface area where
  proprietary code could leak via an accidental import.

### 3.2 Replace `krl_*` imports with direct `requests` calls inside the notebooks

Rewrite each notebook so that data acquisition uses plain `requests` against
FRED/BLS, and methodology uses PyPI-native libraries (`statsmodels`,
`econml`, `causalml`, `linearmodels`).

- **Pro:** Eliminates the private dependency entirely; makes the repository
  truly runnable by anyone with an API key.
- **Con:** Defeats the "funnel to the KRL platform" purpose; removes the
  per-notebook tier-gating demonstration that `CHANGELOG.md:3-30`
  describes; throws away the structural parallel between the notebooks and
  the platform they advertise.

### 3.3 Accept the demo-only reality (selected)

Keep the current shape; document the gap explicitly in README, SPEC, and
this ADR; provide the pre-rendered HTML as the public entry point.

- **Pro:** Minimises maintenance cost; preserves the funnel function;
  aligns repository contents with stated purpose.
- **Con:** Persistent mismatch between the "open-source" label and the
  operational reality; external contributors cannot validate their own
  changes end-to-end.

## 4. Consequences

Positive:

- Single source of truth — no "public-lite" fork to keep in sync with the
  internal `Private IP/` workspace.
- Rendered HTML demos (6 files, 4.5 MB total) remain the canonical
  public-facing artefact; they are cheap to host on GitHub Pages and
  sufficient for readers whose goal is *to evaluate methodology*.
- Clear boundary between open-source (Apache-2.0 text) and commercial
  (`krl_*` runtime).

Negative:

- External contributors per `CONTRIBUTING.md` are structurally blocked from
  running their own changes — the PR checklist item "Notebook runs
  end-to-end without errors" (`.github/PULL_REQUEST_TEMPLATE.md:52`)
  cannot be self-verified by non-KRL contributors.
- Documentation claims — e.g. "125+ causal inference models" (`README.md:145`)
  and "68+ authoritative data sources" (`README.md:143`) — are not
  substantiated by anything in this repository (`SPEC.md §16.8`). An
  auditor evaluating the repository in isolation will find the claims
  unprovable here.
- The repository is structurally unsuited for use by researchers who want
  to learn the methods without the platform — contradicting
  `README.md:125-127`.

## 5. Implementation Notes

Already implemented — this ADR documents present state. Enforcement lives in
the bootstrap code at the first code cell of
`notebooks/causal-inference/14-synthetic-control-policy-lab.ipynb` (and its
siblings), which manipulates `sys.path` and falls through to pip-install
commands for packages that do not exist on public PyPI (`SPEC.md §3.4`).

Downstream artefacts that should cite this ADR:

- `README.md` Quick Start (already updated to reference this ADR).
- `CONTRIBUTING.md` development-environment section (calibration target —
  see [`CALIBRATION_REQUIRED.md`](../CALIBRATION_REQUIRED.md)).
- `docs/getting-started.md` (calibration target — same file currently
  echoes the non-existent `requirements.txt` instruction).

## 6. Reversal / Revisit Criteria

Revisit this decision when any of the following becomes true:

- KRL publishes a Community-tier Python package to public PyPI that covers
  at least the three Community-tier notebooks' import surface.
- A strategic decision is taken to position KASS as a **standalone** open-
  source learning resource rather than a platform funnel.
- External-contributor throughput becomes a bottleneck — i.e. the inability
  of non-KRL users to verify their own PRs materially slows the merge queue.
- An academic partnership or grant requires fully reproducible analyses as
  a condition of use.

Trigger owner: maintainers of `<REPO_PATH>/KASS` jointly with KRL platform
leads. Revisit checkpoint: annually or upon any of the above.

## 7. Open Questions

- **Q1:** If a `krl-oss` minimal variant were built (Alternative 3.1), would
  it import the same module names (`krl_core`, `krl_data_connectors`) with
  a reduced feature set, or would it ship under distinct names
  (`krl_oss.core`, `krl_oss.connectors`) to avoid namespace confusion
  with the paid suite? Decision: `<TOKEN_TBD::krl-oss-namespace-strategy>`.
- **Q2:** What is the acceptance bar for "rendered demos are current"?
  Calendar-month? Every release tag? Any commit to a notebook file?
  Decision: `<TOKEN_TBD::rendered-demo-freshness-SLA>`.
- **Q3:** Should the repository Apache-2.0 licence carry an explicit
  exception-or-notice clarifying that the `krl_*` runtime it invokes is
  proprietary? Decision: `<TOKEN_TBD::license-notice-for-krl-runtime>`.
