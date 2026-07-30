# ==========================================================
# COUNTRY EXPLORER
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------

st.set_page_config(
    page_title="Country Explorer",
    page_icon="🌍",
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

# ----------------------------------------------------------
# HEADER
# ----------------------------------------------------------

st.title("🌍 Country Explorer")

st.markdown("""
Explore the electric vehicle market of individual countries.
""")

st.divider()

# ==========================================================
# FILTERS
# ==========================================================

col1,col2,col3 = st.columns(3)

country = col1.selectbox(
    "Country",
    sorted(
        df["region_country"]
        .dropna()
        .astype(str)
        .unique()
    )
)

parameter = col2.selectbox(
    "Parameter",
    sorted(
        df["parameter"]
        .dropna()
        .astype(str)
        .unique()
    )
)

mode = col3.selectbox(
    "Vehicle Type",
    ["All"] + sorted(
        df["mode"]
        .dropna()
        .astype(str)
        .unique()
    )
)

country_df = df[
    df["region_country"] == country
]

country_df = country_df[
    country_df["parameter"] == parameter
]

if mode != "All":

    country_df = country_df[
        country_df["mode"] == mode
    ]

# ==========================================================
# KPI CARDS
# ==========================================================

k1,k2,k3,k4 = st.columns(4)

k1.metric(
    "Years",
    country_df["year"].nunique()
)

k2.metric(
    "Records",
    len(country_df)
)

k3.metric(
    "Average",
    f"{country_df['value'].mean():,.2f}"
)

k4.metric(
    "Maximum",
    f"{country_df['value'].max():,.0f}"
)

st.divider()

# ==========================================================
# TREND
# ==========================================================

st.subheader(f"{parameter} Trend")

trend = (
    country_df
    .groupby("year", as_index=False)["value"]
    .sum()
)

fig = px.line(
    trend,
    x="year",
    y="value",
    markers=True
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# TWO CHARTS
# ==========================================================

left,right = st.columns(2)

with left:

    st.subheader("Vehicle Distribution")

    vehicle = (
        country_df
        .groupby("mode", as_index=False)["value"]
        .sum()
    )

    fig = px.pie(
        vehicle,
        names="mode",
        values="value",
        hole=0.55
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#0E1117"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    st.subheader("Powertrain Distribution")

    power = (
        country_df
        .groupby("powertrain", as_index=False)["value"]
        .sum()
    )

    fig = px.bar(
        power,
        x="powertrain",
        y="value",
        color="powertrain"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#0E1117",
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================================================
# DATA TABLE
# ==========================================================

st.subheader("Filtered Dataset")

st.dataframe(
    country_df,
    use_container_width=True,
    height=350
)