# KASS Notebook Changelog

## 2026-01-06 - Graceful Degradation for Tiered Features

All notebooks with Professional or Enterprise tier features now implement graceful degradation instead of hard errors for users without the required tier.

### Feature: Subscription/Rental Upsell Messaging

When a notebook tries to import a tier-restricted feature:
- **Displays clear upgrade banner** with feature description
- **Shows current vs. required tier** information
- **Offers upgrade paths**:
  - Subscription option ($99/mo Enterprise, $49/mo Professional)
  - Rental option ($29/analysis for Enterprise, $19/session for Professional)
- **Falls back gracefully** where possible (e.g., community connectors)

### Notebooks Updated

| Notebook | Tier Features | Graceful Handling |
|----------|---------------|-------------------|
| NB11 (Heterogeneous Treatment Effects) | `krl_policy.TreatmentEffectEstimator` | ✓ Enterprise fallback |
| NB14 (Synthetic Control) | `krl_policy.SyntheticControlMethod` | ✓ Enterprise fallback |
| NB15 (RDD Toolkit) | `FREDFullConnector` | ✓ Professional fallback (→ FREDBasicConnector) |
| NB20 (Opportunity Zones) | `krl_policy.TreatmentEffectEstimator` | ✓ Enterprise fallback |
| NB22 (Workforce ROI) | `krl_policy.TreatmentEffectEstimator` | ✓ Enterprise fallback |

---

## 2026-01-04 - Audit Remediation

All notebooks underwent independent audit and remediation to meet institutional standards for transparency, reproducibility, and methodological rigor.

### NB07: Labor Market Intelligence (C+ → A-)

- **FIXED**: Removed demo data fallbacks (now requires valid API keys with RuntimeError on failure)
- **ADDED**: Methodology justification for index weights with academic citations (Bartik 1991, Katz & Murphy 1992, Autor 2019)
- **ADDED**: Threshold sensitivity analysis (0.30-0.50) with explicit "HIGHLY sensitive" interpretation
- **ADDED**: Data provenance badge
- **ENHANCED**: References section with 12+ citations

### NB22: Workforce Development ROI (B+ → A-)

- **ADDED**: Prominent methodological demonstration warning with pre-programmed effect disclosure
- **ADDED**: Cinelli-Hazlett (2020) omitted variable bias sensitivity analysis
- **UPDATED**: Cost-benefit parameters now cite OMB Circular A-4, JobCorps, Card et al. (2018) meta-analysis
- **REMOVED**: Tier marketing language from analytical sections
- **REMOVED**: A+ self-assessment certificate
- **ADDED**: Data provenance badge
- **ENHANCED**: Warning box now explicitly notes ROI/BCR inherit simulation limitations

### NB20: Opportunity Zone Evaluation (B+ → A)

- **ADDED**: Hybrid data structure disclosure with component-by-component provenance table
- **ADDED**: CRITICAL LIMITATIONS section on county-level aggregation bias
- **ADDED**: Pre-programmed effects documentation with actual code reference
- **ADDED**: Data provenance badge
- **ENHANCED**: Limitations now note compounded bias in cost-benefit calculations

---

## Quality Standards Met

All remediated notebooks now comply with:

- **CONTRIBUTING.md** template requirements
- **Institutional-grade transparency** for data provenance
- **Academic citation standards** for methodology choices
- **Explicit limitations disclosure** per KASS standards

---

## Audit Review Summary

| Notebook | Pre-Audit Grade | Post-Audit Grade | Key Improvements |
|----------|-----------------|------------------|------------------|
| NB07 | C+ | A- | API requirements, methodology citations, sensitivity analysis |
| NB20 | B+ | A | Hybrid data disclosure, county-level limitations, ROI caveat |
| NB22 | B+ | A- | Simulated data warning, Cinelli-Hazlett sensitivity, parameter citations |

---

*For full audit report, see internal documentation.*
