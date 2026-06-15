# Methodology

## 1. Measurement Problem

The business problem is healthcare lead generation. The target KPI is qualified calls, with appointment bookings as a secondary downstream signal. Because healthcare demand is affected by seasonality, operational availability, competitive dynamics, and tracking reliability, media variables are not allowed to explain all demand variation.

## 2. Data Design

The dataset has 104 weekly observations. It includes four paid media channels, one primary KPI, one secondary KPI, and control variables.

Media channels:
- Google Search: demand capture, shorter adstock, stronger immediate response.
- Meta: mixed prospecting and retargeting, moderate carryover.
- YouTube: upper-funnel, longer carryover, higher saturation uncertainty.
- Display: always-on support, modest direct response, moderate carryover.

Control variables:
- flu season index;
- holiday indicator;
- back-to-school indicator;
- clinic capacity proxy;
- competitor pressure proxy;
- tracking disruption flag.

## 3. Model Specification

A practical MMM can be written as:

y_t = baseline_t + controls_t + sum(channel_contribution_t) + error_t

Each media channel contribution is modeled through two transformations:

1. Adstock/carryover: current media effect depends on current and prior spend.
2. Saturation: incremental response decreases as spend rises.

## 4. Priors

For healthcare lead generation, priors should be conservative:
- media effects should generally be positive;
- search should have shorter lag than YouTube;
- upper-funnel channels should have wider uncertainty;
- baseline and controls should prevent media from absorbing organic demand;
- ROI priors should avoid implausible returns in sparse data.

## 5. Validation

The validation layer should include:
- posterior predictive checks;
- holdout period performance;
- residual autocorrelation checks;
- contribution plausibility checks;
- ROI sanity ranges;
- spend-response curve review;
- calibration with lift tests, geo tests, or business constraints when available.

## 6. Business Translation

The model should not end with coefficients. It should translate into:
- channel contribution;
- ROI;
- marginal ROI;
- saturation curves;
- budget recommendations;
- uncertainty and limitations.
