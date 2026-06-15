# Healthcare Limitations and Risk Controls

## Data Risks

Healthcare marketing data often includes:
- call-tracking breaks;
- duplicate call handling;
- call quality classification drift;
- appointment capacity constraints;
- lead quality differences by channel;
- HIPAA and privacy limitations;
- incomplete offline conversion feedback.

## Model Risks

MMM is an aggregate observational model. It can estimate plausible contribution, but without experiments it cannot fully separate correlated media effects.

## Recommended Controls

- Keep a tracking quality flag.
- Include clinic capacity when possible.
- Separate qualified calls from raw calls.
- Track booked appointments as secondary KPI.
- Use conservative priors for channels with weak variation.
- Add lift tests when channels are correlated.
- Report uncertainty, not only point estimates.

## Business-Safe Language

Use:
- "estimated contribution";
- "expected marginal return";
- "posterior uncertainty";
- "calibration recommended";
- "decision-support model".

Avoid:
- "proved causality";
- "exact channel attribution";
- "guaranteed ROI";
- "perfect budget optimization".
