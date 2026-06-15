import json
from pathlib import Path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/processed/healthcare_lead_gen_weekly_mmm.csv"
ROI = ROOT / "outputs/channel_roi_summary.csv"
BUDGET = ROOT / "outputs/budget_recommendation.csv"
FIGURES = ROOT / "figures"

st.set_page_config(page_title="Healthcare MMM Executive Dashboard", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #07131F; color: #F6F0E6; }
h1, h2, h3 { color: #F6F0E6; }
[data-testid="stMetricValue"] { color: #B88A3D; }
[data-testid="stMetricLabel"] { color: #D9DEE5; }
</style>
""", unsafe_allow_html=True)

st.title("Healthcare Lead Generation MMM")
st.caption("PyMC-Marketing reference implementation - ROI, marginal return, saturation and budget allocation")

df = pd.read_csv(DATA, parse_dates=["week_start"])
roi = pd.read_csv(ROI)
budget = pd.read_csv(BUDGET)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Qualified Calls", f"{df['qualified_calls'].sum():,.0f}")
c2.metric("Appointment Bookings", f"{df['appointment_bookings'].sum():,.0f}")
c3.metric("Media Spend", f"${df['total_media_spend'].sum()/1000:,.0f}k")
c4.metric("Avg Cost / Qualified Call", f"${df['cost_per_qualified_call_observed'].mean():,.0f}")

st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Executive Summary", "Contribution", "ROI / mROAS", "Saturation", "Budget Recommendation"
])

with tab1:
    st.subheader("Executive Summary")
    st.image(str(FIGURES / "01_executive_kpi_spend.png"))
    st.image(str(FIGURES / "08_executive_scorecard.png"))

with tab2:
    st.subheader("Contribution Decomposition")
    st.image(str(FIGURES / "03_contribution_decomposition.png"))

with tab3:
    st.subheader("ROI and Marginal Return")
    st.image(str(FIGURES / "04_roi_mroas.png"))
    st.dataframe(roi, use_container_width=True)

with tab4:
    st.subheader("Response Curves and Saturation")
    st.image(str(FIGURES / "05_saturation_curves.png"))
    st.image(str(FIGURES / "09_media_correlation_risk.png"))

with tab5:
    st.subheader("Recommended Weekly Budget Reallocation")
    st.image(str(FIGURES / "06_budget_reallocation.png"))
    st.dataframe(budget, use_container_width=True)

st.divider()
st.caption("Disclosure: This dashboard uses simulated data for a portfolio reference implementation. It is not real patient, provider, or client data.")
