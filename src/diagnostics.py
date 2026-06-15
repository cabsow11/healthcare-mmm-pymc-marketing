"""Diagnostics helpers for MMM projects."""

import pandas as pd
import numpy as np

def summarize_missingness(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "column": df.columns,
        "missing_count": df.isna().sum().values,
        "missing_rate": df.isna().mean().values,
    }).sort_values("missing_rate", ascending=False)

def media_correlation(df: pd.DataFrame, channel_columns):
    return df[channel_columns].corr()

def holdout_split(df: pd.DataFrame, holdout_weeks: int = 12):
    train = df.iloc[:-holdout_weeks].copy()
    test = df.iloc[-holdout_weeks:].copy()
    return train, test

def mape(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    return np.mean(np.abs((y_true - y_pred) / np.maximum(np.abs(y_true), 1e-9)))
