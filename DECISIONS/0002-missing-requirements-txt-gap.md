# ADR-0002: The missing `requirements.txt` — formal record of gap

- **Status:** Accepted (documenting present reality; remediation pending)
- **Date:** 2026-04-23
- **Deciders:** Khipu Research Labs engineering
- **Supersedes:** n/a
- **Superseded by:** n/a

---

## 1. Context

Two user-facing touchpoints in this repository instruct users to install
dependencies via `pip install -r requirements.txt`:

- `README.md:38` — the Quick Start fenced block.
- `docs/getting-started.md:28-30` — the Getting Started page shipped to
  GitHub Pages.

A third touchpoint *presumes* the file's eventual existence:
`.github/PULL_REQUEST_TEMPLATE.md:69` — checklist item
"Requirements.txt updated if new packages added."

The file does not exist. `SPEC.md §3.2` records the verification:

```
find /Users/bcdelo/Documents/GitHub/KRL/KASS \
  -name 'requirements*.txt' -o -name 'pyproject.toml' \
  -o -name 'environment.yml' -o -name 'setup.py' \
  -o -name 'Pipfile*'        -o -name 'poetry.lock'
```

returns **zero** results outside `.git/`. A literal first-time user who
follows README step-by-step will hit:

```
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
```

within the first five minutes of onboarding. This is — unambiguously — a
broken quick-start experience. It is also documented, recoverable, and
scoped: the notebook imports are a closed set and can be transcribed into
a manifest.

The underlying authored dependency set is not disputed. `SPEC.md §3.3`
enumerates it:

- **Always present:** `pandas`, `numpy`, `matplotlib.pyplot`, `seaborn`,
  `scipy`, `python-dotenv`.
- **In 5 of 6 notebooks:** `scikit-learn`, `plotly.{express,graph_objects,subplots}`.
- **KRL private suite** (covered separately under ADR-0001): `krl_core`,
  `krl_data_connectors`, `krl_models` (NB07), `krl_enterprise` (NB20, NB22),
  `krl_policy` (NB11), `krl_causal_policy` (NB14, NB15).
- **Named by `CONTRIBUTING.md:37` but imported by zero notebooks:**
  `statsmodels`, `econml`, `causalml` (`SPEC.md §6.1`, `§16.8`).

## 2. Decision

Formally recognise the missing `requirements.txt` as a **documented gap**,
not a stylistic choice, and queue it for remediation. Until remediation,
all three citing surfaces MUST carry an inline advisory that the file does
not exist and point at the practical substitute block.

The deferred implementation work (tracked in
[`CALIBRATION_REQUIRED.md`](../CALIBRATION_REQUIRED.md)) is to produce a
pinned `requirements.txt` (and optionally `requirements-dev.txt`) that
exactly matches the importable surface in `SPEC.md §3.3` and `§4`, with
`statsmodels`/`econml`/`causalml` either removed from `CONTRIBUTING.md` or
actually adopted by at least one notebook.

## 3. Alternatives Considered

### 3.1 Commit a minimal `requirements.txt` today (deferred — not executed in this ADR)

Ship a file containing only the eight third-party PyPI packages actually
imported, plus `black` (named in `CONTRIBUTING.md:37, 191-193, 270`).

- **Pro:** Immediate fix; Quick Start becomes truthful.
- **Con:** Requires a version-pinning decision (floor versus floor-ceiling
  versus exact pins) that has not yet been taken; interacts with ADR-0001's
  private-suite gap (a `requirements.txt` that only installs the public
  deps still doesn't make the notebooks runnable).

### 3.2 Migrate to `pyproject.toml` (PEP 621)

Adopt a modern Python packaging layout even though the repository is not
intended to be a package — using `[project.optional-dependencies]` to
describe the notebook environment.

- **Pro:** Forward-compatible with Poetry / Hatch / PDM / uv; lockfile
  semantics available; tool-configuration centralisation (black, ruff).
- **Con:** Implies a package identity (`name`, `version`) that the
  repository explicitly disclaims (`SPEC.md §1`, §3.2 first paragraph).
  Overkill for a six-notebook demo repo.

### 3.3 Document the current state; defer the file (selected for this ADR)

Keep the repository in its current shape; add inline advisories to the
three citing surfaces; log a CALIBRATION action.

- **Pro:** Honest with users within one commit; decouples the content
  decision (what to pin, how) from the documentation decision (stop lying
  to new users).
- **Con:** The underlying gap remains; users still can't `pip install` via
  the advertised one-liner.

## 4. Consequences

Positive:

- Formal recording of the gap means future contributors cannot treat the
  advertised `pip install -r requirements.txt` as correct; the ADR acts as
  a prompt to finish the job.
- Decoupling advisory (low risk, immediate) from implementation (requires
  decisions about pinning strategy) lets the repo ship honest docs today.

Negative:

- Users who skim the README past the advisory will still hit the error.
- The PR-template checklist item persists as a phantom obligation until
  the file exists or the item is removed.
- External contributors who want to add a dependency have nowhere to add
  it except the two documentation surfaces — encouraging further drift.

## 5. Implementation Notes

### 5.1 Advisories added in this commit

- `README.md` Known Advisories block (§1) — inline, above the Quick Start.
- `README.md` Quick Start — trailing comment on the `pip install -r` line.
- Cross-reference to this ADR from
  [`CALIBRATION_REQUIRED.md`](../CALIBRATION_REQUIRED.md) and
  [`policy/dependency.yaml`](../policy/dependency.yaml).

### 5.2 Remediation checklist (to execute outside this ADR)

1. Decide pinning strategy: `<TOKEN_TBD::req-txt-pin-strategy>`
   (floor-only, floor+ceiling, exact-pin).
2. Generate an initial manifest from `SPEC.md §3.3` + `§4`; include only
   packages actually imported.
3. Either remove `statsmodels`, `econml`, `causalml` from
   `CONTRIBUTING.md:37` **or** introduce them into at least one notebook.
4. Update `docs/getting-started.md:28-30` to reference the new file.
5. Remove the advisories added in §5.1 once the file ships.
6. Strike through this ADR's "Accepted — remediation pending" status and
   mark it "Superseded by: ADR-00NN" (the ADR that ships the file).

## 6. Reversal / Revisit Criteria

This ADR is a stopgap. It should be **superseded** once `requirements.txt`
exists and is verified by a fresh clone walking through the Quick Start
without editing the command. Reversal — i.e. deliberately removing the
file again — would only be reasonable if the repository migrated to
`pyproject.toml` (Alternative 3.2), in which case a new ADR captures the
migration.

## 7. Open Questions

- **Q1:** Pin strategy — see `<TOKEN_TBD::req-txt-pin-strategy>` above.
- **Q2:** Do we ship `requirements-dev.txt` separately (for `black`,
  `jupyter`, `nbconvert`) or fold everything into a single file?
  Decision: `<TOKEN_TBD::req-dev-split-strategy>`.
- **Q3:** Should `requirements.txt` include the `krl_*` suite as a
  best-effort entry referencing a private index URL (documented but
  unresolved for external users), or omit them entirely and rely on the
  existing `KRL_DEV_PATH` bootstrap? Decision:
  `<TOKEN_TBD::krl-suite-in-requirements-strategy>`.
