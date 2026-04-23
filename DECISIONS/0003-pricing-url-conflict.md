# ADR-0003: Pricing URL host conflict — canonical URL unresolved

- **Status:** Accepted (documenting present reality; canonical URL pending)
- **Date:** 2026-04-23
- **Deciders:** Khipu Research Labs engineering
- **Supersedes:** n/a
- **Superseded by:** n/a

---

## 1. Context

The KASS repository publishes pricing information through at least three
surfaces, which disagree on the canonical host:

| Surface | Host | Evidence |
|---------|------|----------|
| README "View Interactive Pricing" link | `bcdelodx.github.io/KASS/pricing.html` (personal account) | `README.md:183` |
| Repository Jekyll site base URL | `khipuresearch.github.io/KASS/` (organisation account) | `docs/_config.yml:4-5`, `README.md:16` |
| Root `pricing.html` file | present in-repo at repo root | `SPEC.md §5`, `SPEC.md §14.1` |
| Stripe Payment Link URLs | documented placeholders (`https://buy.stripe.com/krl_pro_monthly`, etc.) | `CHANGELOG.md:13-17`, `CHANGELOG.md:20` |

Three facts follow from this:

1. The file `pricing.html` lives at the **repository root**, not under
   `docs/`. The Jekyll build at `docs/_config.yml` does **not** pick up
   root-level files, so `khipuresearch.github.io/KASS/pricing.html`
   publishes only if a separate GitHub Pages site is serving the root of
   the repo — which this workflow topology does not do
   (`.github/workflows/pages.yml` builds `docs/` only).
2. `bcdelodx.github.io/KASS/pricing.html` is reachable **only if** the
   personal `bcdelodx` account runs its own Pages deployment from a fork
   or mirror of this repository with root-file publication enabled. That
   configuration lives outside this repository and is not reproducible
   from in-tree artefacts.
3. The Stripe links referenced in `CHANGELOG.md:13-17` are explicit
   placeholders (`CHANGELOG.md:20`: "Replace placeholder URLs with actual
   Stripe Payment Links from your dashboard"). A user clicking through
   from a notebook's graceful-degradation banner today does not reach a
   live checkout.

Severity: medium. The README's marketing call-to-action links to an
external, personally-owned host that is not controlled by the same
governance as the rest of the repository, and whose lifecycle is opaque.
If the personal account is retired, renamed, or revokes Pages, every
README-surface pricing link 404s silently.

## 2. Decision

Pricing-surface topology is **unresolved**. This ADR records the conflict,
forbids further additions to the unresolved state, and defines the
decision space that must be navigated to resolve it. Until resolution, the
README MUST carry a visible inline advisory (already added in the same
commit as this ADR) noting the host mismatch.

Specifically:

1. No new reference to `bcdelodx.github.io/KASS/pricing.html` may be added
   to any in-repo file.
2. No new host may be introduced for pricing without superseding this ADR.
3. The Stripe placeholder URLs in `CHANGELOG.md:13-17` must remain
   flagged as placeholders until real Stripe Payment Links replace them.
4. The `pricing.html` file at repo root must either (a) be moved under
   `docs/` so the Jekyll build publishes it at a known URL, or (b) be
   removed, depending on the resolution chosen below.

## 3. Alternatives Considered

### 3.1 Move `pricing.html` into `docs/` and canonicalise `khipuresearch.github.io/KASS/pricing.html`

Relocate the file to `docs/pricing.html` (or `docs/pricing.md` with Jekyll
front-matter). Update `README.md:183` and every outbound reference. Treat
`khipuresearch.github.io/KASS/pricing.html` as the single canonical URL.

- **Pro:** Governance aligns with the rest of the site. Single deployment
  pipeline. Personal-account host can be retired.
- **Con:** Requires coordination with any existing outbound-traffic source
  (Stripe, ads, partner pages) that currently points at `bcdelodx.github.io`.

### 3.2 Move pricing to an external KRL-owned domain (`pricing.krlabs.dev`)

Remove `pricing.html` from the repository entirely. Maintain the pricing
page on the commercial KRL site. Replace every in-repo link with the
external URL.

- **Pro:** Separates marketing asset from open-source content; aligns
  pricing-page lifecycle with the commercial product; enables A/B testing
  and other marketing infrastructure that doesn't belong in a static-docs
  repo.
- **Con:** Adds an external dependency to the open-source repo's
  call-to-action; requires hosting infrastructure outside GitHub Pages.

### 3.3 Keep the current topology; accept the personal-account link (rejected)

Leave everything as-is.

- **Pro:** Zero engineering work.
- **Con:** Fragile (personal-account host); inconsistent with the rest of
  the repository; a new reader has no way to determine which URL is
  "correct." Audit-hostile.

## 4. Consequences

Positive (of recording the decision to resolve):

- Explicit acknowledgement that the README's top-line call-to-action
  currently points at a weak link.
- Clear decision-gate: any future PR adding a pricing link must select
  from Alternative 3.1 or 3.2 (or supersede this ADR).
- Downstream YAMLs ([`policy/access-control.yaml`](../policy/access-control.yaml))
  can reference this ADR as the source-of-truth for who approves a
  host-change PR.

Negative:

- Until resolution, external readers encounter a mismatched set of URLs
  and must trust the README advisory at face value.
- The existing placeholder Stripe URLs in `CHANGELOG.md:13-17` continue
  to be non-functional; tier-gated-feature banners in the notebooks
  (`CHANGELOG.md:9-20`) inherit that non-functionality.

## 5. Implementation Notes

### 5.1 Advisories added in this commit

- `README.md` Known Advisories block (§1, item 3) — inline, points at this
  ADR.
- `README.md` Pricing section — quote block warning that the URL is
  unresolved.

### 5.2 Remediation checklist (to execute outside this ADR)

1. Decide between Alternative 3.1 (move under `docs/`) and 3.2 (move to
   external KRL-owned host): `<TOKEN_TBD::pricing-host-canonicalisation>`.
2. If 3.1: relocate `pricing.html` → `docs/pricing.html`, ensure Jekyll
   includes it, update `docs/_config.yml` navigation if required, update
   `README.md:183`, delete the root-level `pricing.html`.
3. If 3.2: delete root-level `pricing.html`, point all references at
   `<TOKEN_TBD::external-pricing-host-URL>`.
4. Replace every placeholder Stripe URL in `CHANGELOG.md:13-17` with a
   live Payment Link, or move those URL references entirely out of the
   repository into the (private) KRL platform code.
5. Add an outbound-link check to `.github/workflows/pages.yml` (or a new
   lint workflow) that fails on any URL containing `bcdelodx.github.io`.
6. Supersede this ADR with a successor.

## 6. Reversal / Revisit Criteria

Revisit when any of the following becomes true:

- A successor ADR selects Alternative 3.1 or 3.2 and is merged; this ADR
  is then marked "Superseded by: ADR-00NN."
- The personal host `bcdelodx.github.io` is retired and the README link
  begins returning 404; immediate remediation becomes mandatory.
- Stripe Payment Links are finalised and the `CHANGELOG.md:13-17`
  placeholders are replaced; the pricing-URL decision should then be
  sequenced before any new marketing campaign that drives users to the
  link.

## 7. Open Questions

- **Q1:** Which alternative wins — `<TOKEN_TBD::pricing-host-canonicalisation>`?
  Decision owner: marketing lead jointly with repository maintainers.
- **Q2:** If Alternative 3.2: what is the canonical URL —
  `<TOKEN_TBD::external-pricing-host-URL>`?
- **Q3:** Who owns the personal `bcdelodx.github.io` host today, and what
  is the deprecation plan? Decision:
  `<TOKEN_TBD::bcdelodx-host-deprecation-owner>`.
- **Q4:** Should the Stripe Payment Link URLs live in a CI-read secret,
  in `CHANGELOG.md`, in the proprietary `krl_*` code, or on the pricing
  page only? Decision: `<TOKEN_TBD::stripe-payment-link-surface>`.
