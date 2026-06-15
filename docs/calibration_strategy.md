# Calibration Strategy

## Why Calibration Matters

With 18-24 months of weekly data, MMM can be underidentified when channels are correlated. Google and Meta often move together. Without calibration, the model can assign too much credit to the wrong channel.

## Preferred Calibration Signals

1. Lift tests
2. Geo experiments
3. Holdout periods
4. Campaign pause tests
5. Incrementality tests
6. Prior business constraints on ROI
7. Known operational events

## Recommended First Client Question

Do you have any calibration signal available, such as lift tests, geo tests, holdout periods, campaign experiments, or prior business constraints on expected ROI by channel, or should the first version rely mainly on domain-informed priors, posterior predictive validation, and business plausibility checks?

## Practical Calibration Workflow

1. Fit uncalibrated MMM.
2. Review correlation and contribution plausibility.
3. Add lift test measurements where available.
4. Refit and compare posterior channel contributions.
5. Stress-test budget recommendations under conservative and aggressive scenarios.
6. Document what changed and why.
