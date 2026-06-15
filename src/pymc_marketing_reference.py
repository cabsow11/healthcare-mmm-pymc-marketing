"""PyMC-Marketing MMM implementation template.

This file is intentionally explicit. It is designed to be adapted to the client's
SageMaker container and current PyMC-Marketing version.

Expected input columns:
- date column: week_start
- channel columns: google_search_spend, meta_spend, youtube_spend, display_spend
- target: qualified_calls
- controls: flu_season_index, holiday_week, back_to_school_week, clinic_capacity_index,
  competitor_pressure_index, tracking_disruption_flag
"""

import pandas as pd

CHANNEL_COLUMNS = [
    "google_search_spend",
    "meta_spend",
    "youtube_spend",
    "display_spend",
]

CONTROL_COLUMNS = [
    "flu_season_index",
    "holiday_week",
    "back_to_school_week",
    "clinic_capacity_index",
    "competitor_pressure_index",
    "tracking_disruption_flag",
]

TARGET = "qualified_calls"
DATE_COLUMN = "week_start"

def build_pymc_marketing_mmm(df: pd.DataFrame):
    """Build a PyMC-Marketing MMM object.

    This function uses current PyMC-Marketing concepts:
    - MMM model class
    - GeometricAdstock
    - LogisticSaturation
    - control columns
    - date column

    Exact keyword names may need a minor adjustment depending on the installed
    PyMC-Marketing version in the client's SageMaker container.
    """
    from pymc_marketing.mmm import GeometricAdstock, LogisticSaturation
    from pymc_marketing.mmm.multidimensional import MMM

    X = df[[DATE_COLUMN] + CHANNEL_COLUMNS + CONTROL_COLUMNS].copy()
    y = df[TARGET].copy()

    mmm = MMM(
        date_column=DATE_COLUMN,
        channel_columns=CHANNEL_COLUMNS,
        control_columns=CONTROL_COLUMNS,
        adstock=GeometricAdstock(l_max=8),
        saturation=LogisticSaturation(),
    )
    return mmm, X, y

def fit_model(df: pd.DataFrame, draws: int = 1000, tune: int = 1000, chains: int = 4):
    """Fit MMM and return fitted object."""
    mmm, X, y = build_pymc_marketing_mmm(df)
    idata = mmm.fit(X=X, y=y, draws=draws, tune=tune, chains=chains, target_accept=0.9)
    return mmm, idata

def add_lift_tests_and_refit(mmm, X, y, lift_test_df, fit_kwargs=None):
    """Optional calibration workflow if client has lift tests."""
    fit_kwargs = fit_kwargs or {"draws": 1000, "tune": 1000, "chains": 4, "target_accept": 0.9}
    mmm.build_model(X, y)
    mmm.add_lift_test_measurements(df_lift_test=lift_test_df)
    idata = mmm.fit(X, y, **fit_kwargs)
    return mmm, idata
