# ==========================================================
# EXECUTIVE INSIGHTS
# ==========================================================

import streamlit as st
import pandas as pd
from pathlib import Path

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------

st.set_page_config(
    page_title="Executive Insights",
    page_icon="💼",
    layout="wide"
)

# ----------------------------------------------------------
# LOAD DATA
# ----------------------------------------------------------

@st.cache_data
def load_data():

    project_dir = Path(__file__).resolve().parents[2]

    data_path = (
        project_dir
        / "data"
        / "processed"
        / "ev_analysis_ready.csv"
    )

    return pd.read_csv(data_path)

df = load_data()

# ==========================================================
# HEADER
# ==========================================================

st.title("💼 Executive Insights")

st.markdown("""
A consolidated summary of the Global EV Intelligence Dashboard.
This page highlights the most important findings from the complete
analysis and provides strategic recommendations for decision-makers.
""")

st.divider()

# ==========================================================
# EXECUTIVE KPI CARDS
# ==========================================================

sales = df[
    (df["parameter"]=="EV sales") &
    (df["Aggregate group"]=="_World") &
    (df["mode"]=="Cars") &
    (df["powertrain"]=="EV") &
    (df["year"]==2025)
]["value"].sum()

stock = df[
    (df["parameter"]=="EV stock") &
    (df["Aggregate group"]=="_World") &
    (df["mode"]=="Cars") &
    (df["powertrain"]=="EV") &
    (df["year"]==2025)
]["value"].sum()

countries = df["region_country"].nunique()

parameters = df["parameter"].nunique()

k1,k2,k3,k4 = st.columns(4)

k1.metric(
    "Global EV Sales",
    f"{sales/1_000_000:.1f} M"
)

k2.metric(
    "Global EV Stock",
    f"{stock/1_000_000:.1f} M"
)

k3.metric(
    "Countries",
    countries
)

k4.metric(
    "Business Indicators",
    parameters
)

st.divider()

# ==========================================================
# KEY FINDINGS
# ==========================================================

st.subheader("📌 Key Findings")

st.info("""

### Global Market

- Passenger EV sales reached approximately **21 million vehicles** in 2025.
- Global passenger EV stock exceeded **75 million vehicles**.
- Passenger cars remain the dominant EV segment worldwide.

### Technology

- Battery Electric Vehicles (BEVs) dominate the global market.
- Government policies continue to accelerate EV adoption.
- Vehicle prices show significant variation across countries.

### Infrastructure

- Charging infrastructure has expanded steadily.
- Electricity demand is expected to increase alongside EV adoption.
- Battery deployment continues to grow with market expansion.

### Forecast

- Under the **Current Policies Scenario (CPS)**, EV stock is projected to exceed **450 million** by 2035.
- Under the **Stated Policies Scenario (STEPS)**, EV stock approaches **470 million** by 2035.
- Stronger policy support leads to higher market growth.

""")

st.divider()

# ==========================================================
# STRATEGIC RECOMMENDATIONS
# ==========================================================

st.subheader("🚀 Strategic Recommendations")

gov, industry = st.columns(2)

with gov:

    st.success("""

### Governments

- Continue supporting EV incentive programs.
- Expand charging infrastructure.
- Strengthen renewable energy integration.
- Encourage battery recycling initiatives.
- Promote long-term EV policy stability.

""")

with industry:

    st.success("""

### Industry

- Increase production capacity.
- Focus on affordable EV models.
- Invest in battery innovation.
- Expand charging partnerships.
- Improve supply-chain resilience.

""")

st.divider()

# ==========================================================
# INVESTMENT OPPORTUNITIES
# ==========================================================

st.subheader("📈 Investment Opportunities")

st.warning("""

High-potential investment areas include:

- Public charging infrastructure
- Battery manufacturing
- Renewable energy integration
- Smart grid technologies
- EV software and connected services
- Fleet electrification
- Energy storage systems

""")

st.divider()

# ==========================================================
# PROJECT SUMMARY
# ==========================================================

st.subheader("📚 Project Summary")

summary = pd.DataFrame({

    "Component":[

        "Notebook 1",

        "Notebook 2",

        "Notebook 3",

        "Dashboard"

    ],

    "Description":[

        "Data Audit & Preprocessing",

        "Exploratory Data Analysis",

        "Forecasting & Future Outlook",

        "Interactive Business Intelligence Dashboard"

    ],

    "Status":[

        "Completed",

        "Completed",

        "Completed",

        "Completed"

    ]

})

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# FINAL CONCLUSION
# ==========================================================

st.subheader("🎯 Final Conclusion")

st.success("""

The Global EV Intelligence Dashboard demonstrates the rapid evolution
of the electric vehicle market from 2010 to 2035 using the
International Energy Agency (IEA) Global EV Outlook dataset.

The analysis integrates historical trends, infrastructure development,
pricing intelligence, vehicle technologies, and future policy scenarios
into a single decision-support platform.

The results indicate sustained growth in global EV adoption, increasing
requirements for charging infrastructure and electricity demand, and
stronger market expansion under ambitious policy scenarios.

This dashboard provides a practical business intelligence solution for
governments, manufacturers, investors, researchers, and policymakers.

""")

st.divider()

st.caption(
    "Global EV Intelligence Dashboard | Developed using Streamlit & Plotly"
)