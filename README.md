# Healthcare Lead Generation MMM with PyMC-Marketing

**Premium portfolio reference implementation for a healthcare lead-generation Marketing Mix Model.**

This repository demonstrates how a healthcare measurement startup can build a first Bayesian MMM pipeline using PyMC-Marketing-style modeling, weekly media data, call-tracking outcomes, conservative priors, validation logic, and a Streamlit executive dashboard.

The project is built around a 24-month weekly dataset that is simulated but intentionally realistic: it includes seasonality, Google/Meta correlation, YouTube flighting, display always-on support, upper-funnel carryover, diminishing returns, clinic capacity constraints, competitive pressure, and a short call-tracking disruption.

## Executive Objective

The objective is not to produce the most complex model possible. The objective is to produce a robust and interpretable measurement layer that helps a healthcare marketing team answer four questions:

1. Which channels contributed to qualified calls?
2. What is the expected ROI and marginal ROI by channel?
3. Where are channels approaching saturation?
4. How should the next weekly budget be reallocated under uncertainty?

## Repository Structure

```text
healthcare_mmm_pymc_marketing_premium/
├── data/
│   ├── raw/simulated_client_export_healthcare_mmm.csv
│   └── processed/healthcare_lead_gen_weekly_mmm.csv
├── docs/
│   ├── methodology.md
│   ├── model_assumptions.md
│   ├── calibration_strategy.md
│   ├── healthcare_limitations.md
│   ├── sagemaker_delivery_plan.md
│   └── bibliography.md
├── figures/
├── notebooks/
│   ├── 01_data_simulation.ipynb
│   ├── 02_eda_and_validation.ipynb
│   ├── 03_pymc_marketing_mmm.ipynb
│   └── 04_budget_optimization.ipynb
├── outputs/
├── proposal/
├── reports/Healthcare_MMM_Executive_Report.pdf
├── src/
│   ├── simulate_data.py
│   ├── transformations.py
│   ├── pymc_marketing_reference.py
│   ├── diagnostics.py
│   └── budget_optimizer.py
└── streamlit_app/app.py
```

## Model Design

The model uses the core MMM logic expected in a healthcare measurement engagement:

- weekly KPI: qualified calls;
- paid media channels: Google Search, Meta, YouTube, Display;
- media transformations: adstock/carryover and saturation;
- controls: seasonality, holidays, clinic capacity, competitive pressure, tracking disruption;
- outputs: contribution, ROI, mROAS, saturation curves, and budget recommendations;
- validation: posterior predictive checks, holdout logic, contribution sanity checks, and calibration plan.

## Main Business Outputs

| Output | Business Use |
|---|---|
| Channel contribution | Explains which channels drove qualified calls |
| ROAS and mROAS | Separates historical efficiency from next-dollar efficiency |
| Saturation curves | Shows where scaling may stop being efficient |
| Budget recommendation | Provides a conservative reallocation scenario |
| Data quality matrix | Makes tracking and operational risks visible |

## Methodological Positioning

This implementation is designed around a practical market-response philosophy: standardized enough to be reusable, simple enough to be explainable, and robust enough to avoid implausible answers. It treats MMM as decision support under uncertainty, not as deterministic attribution.

## Important Disclosure

This repository uses simulated data. It is designed as a reference implementation for portfolio demonstration, technical evaluation, and client scoping. It should not be presented as real client data.

## Portfolio Summary

> I maintain a healthcare-oriented PyMC-Marketing MMM reference implementation for lead generation measurement. It uses 24 months of weekly simulated-but-realistic data across Google Search, Meta, YouTube, and Display, with qualified calls and appointment bookings as KPIs. The model includes adstock, saturation, priors, validation logic, ROI/mROAS outputs, budget allocation, and a Streamlit dashboard.
