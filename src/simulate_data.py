"""Generate the simulated healthcare MMM dataset.

This file mirrors the dataset included in data/processed.
Run from repository root:
    python src/simulate_data.py
"""

from pathlib import Path
import numpy as np
import pandas as pd
from transformations import geometric_adstock, logistic_saturation

def build_dataset(seed: int = 1447, n: int = 104) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2024-01-01", periods=n, freq="W-MON")
    t = np.arange(n)

    flu = np.clip(0.5 + 0.5*np.cos(2*np.pi*(t-6)/52), 0, 1)
    holiday = (((dates.month == 11) & (dates.day >= 18)) | (dates.month == 12) | ((dates.month == 1) & (dates.day <= 10))).astype(int)
    bts = (((dates.month == 8) & (dates.day >= 1)) | ((dates.month == 9) & (dates.day <= 15))).astype(int)
    capacity = np.clip(0.94 + 0.055*np.sin(2*np.pi*(t+7)/52) + rng.normal(0, 0.015, n), 0.80, 1.08)
    competitor = np.clip(0.47 + 0.16*np.sin(2*np.pi*(t+17)/26) + rng.normal(0, 0.045, n), 0.13, 0.92)

    def pulse(center, width, height):
        return height*np.exp(-0.5*((t-center)/width)**2)

    flights = pulse(12, 3.5, 1.0) + pulse(31, 4.5, 1.15) + pulse(50, 4, 1.3) + pulse(66, 4, 1.1) + pulse(84, 5, 1.25) + pulse(96, 4, 0.75)
    google = np.clip(11000 + 1050*t/n + 1700*flu + 900*flights + 700*holiday + rng.normal(0, 900, n), 5600, 19200)
    meta_raw = 6100 + 620*np.sin(2*np.pi*t/52) + 1550*flights + 850*bts + rng.normal(0, 870, n)
    meta = np.clip(0.24*google + 0.76*meta_raw, 2600, 14800)
    youtube = np.clip(2400 + 4900*(pulse(18,5,1)+pulse(43,6,1)+pulse(75,6,1)+pulse(95,4,1)) + rng.normal(0, 600, n), 0, 11200)
    display = np.clip(3300 + 360*np.cos(2*np.pi*t/52) + 580*flights + rng.normal(0, 430, n), 1200, 6500)

    tracking = np.ones(n)
    tracking[58:61] = [0.91, 0.82, 0.93]

    params = {
        "google_search_spend": {"alpha": 0.24, "lambda": 4.30, "midpoint": 14500, "scale_calls": 125},
        "meta_spend": {"alpha": 0.47, "lambda": 3.25, "midpoint": 11800, "scale_calls": 92},
        "youtube_spend": {"alpha": 0.72, "lambda": 2.65, "midpoint": 12600, "scale_calls": 59},
        "display_spend": {"alpha": 0.55, "lambda": 2.15, "midpoint": 7600, "scale_calls": 34},
    }
    channels = {
        "google_search_spend": google,
        "meta_spend": meta,
        "youtube_spend": youtube,
        "display_spend": display,
    }

    contrib = []
    output = {
        "week_start": dates,
        "google_search_spend": google,
        "meta_spend": meta,
        "youtube_spend": youtube,
        "display_spend": display,
        "flu_season_index": flu,
        "holiday_week": holiday,
        "back_to_school_week": bts,
        "clinic_capacity_index": capacity,
        "competitor_pressure_index": competitor,
        "tracking_quality_index": tracking,
        "tracking_disruption_flag": (tracking < .95).astype(int),
    }

    for ch, spend in channels.items():
        p = params[ch]
        ad = geometric_adstock(spend, p["alpha"])
        sat = logistic_saturation(ad, p["lambda"], p["midpoint"])
        inc = p["scale_calls"] * sat
        output[ch.replace("_spend", "_adstock")] = ad
        output[ch.replace("_spend", "_saturation")] = sat
        output[ch.replace("_spend", "_true_incremental_calls")] = inc
        contrib.append(inc)

    baseline = 214 + 0.45*t + 23*flu + 10*holiday + 8*bts + 21*(capacity - capacity.mean()) - 19*competitor
    mu = (baseline + sum(contrib)) * tracking
    calls = np.maximum(55, np.round(mu + rng.normal(0, 21, n))).astype(int)
    booking_rate = np.clip(0.34 + 0.03*(capacity-0.94) - 0.015*(competitor-0.47) + rng.normal(0, .012, n), 0.25, 0.45)
    bookings = np.maximum(10, np.round(calls*booking_rate + rng.normal(0, 4, n))).astype(int)

    output["qualified_calls"] = calls
    output["appointment_bookings"] = bookings
    output["baseline_calls_true"] = baseline
    output["total_incremental_calls_true"] = sum(contrib)

    df = pd.DataFrame(output)
    df["total_media_spend"] = df[["google_search_spend", "meta_spend", "youtube_spend", "display_spend"]].sum(axis=1)
    df["cost_per_qualified_call_observed"] = df["total_media_spend"] / df["qualified_calls"]
    df["expected_value_per_qualified_call"] = 225.0
    return df

if __name__ == "__main__":
    out = Path("data/processed")
    out.mkdir(parents=True, exist_ok=True)
    build_dataset().to_csv(out / "healthcare_lead_gen_weekly_mmm.csv", index=False)
