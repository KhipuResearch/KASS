# .github/workflows/

> The CI topology for KASS is narrow by design. One deploy workflow, two
> repository-hygiene workflows. No test, lint, scan, or release jobs run here
> today — `SPEC.md §13, §11.3, §16.7`. This README enumerates what is
> present and cross-references calibration pending in
> [`policy/ci-authority.yaml`](../../policy/ci-authority.yaml).

---

## Workflows Present (3)

### 1. `pages.yml` — Deploy Jekyll site to GitHub Pages

**The single deploy path that exists in this repository.** Cited in
`SPEC.md §6.4` and `.github/workflows/pages.yml:17-59`.

| Attribute | Value |
|-----------|-------|
| Triggers | `push` to `main`; `workflow_dispatch` |
| Permissions | `contents: read`, `pages: write`, `id-token: write` |
| Concurrency | `group: pages`, `cancel-in-progress: false` |
| Build runner | `ubuntu-latest` |
| Ruby | `3.2` (via `ruby/setup-ruby@v1`) |
| Build command | `bundle exec jekyll build --baseurl /KASS` (env `JEKYLL_ENV=production`) |
| Artifact upload | `actions/upload-pages-artifact@v3` from `docs/_site` |
| Deploy | `actions/deploy-pages@v4` into environment `github-pages` |

Notable facts:

- Works from the `docs/` subdirectory; the build step has `working-directory:
  docs` (see `.github/workflows/pages.yml:20-23, 30`).
- No `Gemfile.lock` is committed — CI resolves Gem versions fresh every run
  (`SPEC.md §6.4`; removed in commit `4f8def8`).
- This is the only workflow that can write anything back to the public surface
  of the project.
- Does **not** execute notebooks. Does **not** regenerate `notebook_results/`
  or `docs/demos/*.html`; those files are checked in pre-rendered by a human
  offline (`SPEC.md §6.5`, `SPEC.md §16.3`). See
  [`policy/ci-authority.yaml`](../../policy/ci-authority.yaml)
  → `workflows_absent_but_referenced.nbconvert-render-demos`.

### 2. `issue-management.yml` — Auto-label and welcome

Purpose per `SPEC.md §7.4`: apply method-tagged labels (`method-did`,
`method-synth-control`, `method-rdd`, `method-hte`, `method-iv`,
`method-matching`) and domain-tagged labels (`domain-workforce`,
`domain-education`, `domain-health`, `domain-housing`, `domain-environment`,
`domain-justice`, `domain-economic`) to newly opened issues; remove
`needs-triage` on first label; welcome first-time contributors.

Authority boundary: may read/write issue labels and post comments; may not
modify code, docs, or other workflows. Recorded in
[`policy/ci-authority.yaml`](../../policy/ci-authority.yaml).

### 3. `stale.yml` — Close inactive issues and PRs

Per `SPEC.md §7.3`:

| Object | Days-to-stale | Days-to-close (after stale) |
|--------|---------------|------------------------------|
| Issues | 30 | 14 |
| PRs | 45 | 14 |

Exempt labels: `priority-urgent`, `priority-high`, `in-progress`, `blocked`,
`good-first-issue`, `help-wanted`, `enhancement`. `exempt-all-milestones:
true`.

Authority boundary: same as `issue-management.yml` — label/state/comment on
issues and PRs only.

---

## Workflows *Absent* but Referenced Elsewhere

Every bullet below corresponds to a promise the documentation makes that no
workflow keeps. Each has a calibration token in
[`policy/ci-authority.yaml`](../../policy/ci-authority.yaml):

1. **Test suite runner.** `SPEC.md §13`,
   [`tests/README.md`](../../tests/README.md),
   `.github/PULL_REQUEST_TEMPLATE.md:52-56`. Calibration:
   `<TOKEN_TBD::wire-test-workflow>`.
2. **Notebook rendering.** `SPEC.md §6.5, §16.3` — `notebook_results/*.html`
   timestamps drift from notebook source. Calibration:
   `<TOKEN_TBD::wire-nbconvert-workflow>`.
3. **Outbound-link check.** Would detect the pricing-URL host mismatch
   recorded in
   [`DECISIONS/0003-pricing-url-conflict.md`](../../DECISIONS/0003-pricing-url-conflict.md)
   and the placeholder Stripe URLs in `CHANGELOG.md:13-17`. Calibration:
   `<TOKEN_TBD::wire-link-check-workflow>`.
4. **Dependency audit.** `.github/SECURITY.md:62` instructs users to run
   `pip-audit`; no workflow does. `SPEC.md §16.7`. Calibration:
   `<TOKEN_TBD::wire-pip-audit-workflow>`.
5. **Secret scan.** No `gitleaks` / `trufflehog` / GitHub Advanced Security
   integration is active. Calibration:
   `<TOKEN_TBD::wire-secret-scan-workflow>`.
6. **Notebook diff guard.** `CONTRIBUTING.md:271-272` requires output-cleared
   commits; no workflow verifies. Calibration:
   `<TOKEN_TBD::wire-notebook-diff-guard>`.

---

## Related Artefacts

- [`policy/ci-authority.yaml`](../../policy/ci-authority.yaml) — binding
  policy over what workflows may do.
- [`policy/access-control.yaml`](../../policy/access-control.yaml) — who may
  edit files in this directory. Workflow changes require an ADR.
- [`SPEC.md §6.4, §6.5, §7.3, §7.4`](../../SPEC.md) — forensic record of
  current CI.
- [`DECISIONS/0001-demo-only-no-proprietary-compute.md`](../../DECISIONS/0001-demo-only-no-proprietary-compute.md)
  — the reason a full test-and-render CI cannot run externally today.
