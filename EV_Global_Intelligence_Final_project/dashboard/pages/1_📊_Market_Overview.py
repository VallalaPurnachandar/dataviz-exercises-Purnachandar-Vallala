# ==========================================================
# MARKET OVERVIEW
# Global EV Intelligence Dashboard
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------

st.set_page_config(
    page_title="Market Overview",
    page_icon="📊",
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

st.title("📊 Global Market Overview")

st.markdown(
"""
Explore the historical evolution of the global electric vehicle market.

Use the interactive filters to investigate market trends,
vehicle adoption and charging infrastructure.
"""
)

st.divider()

# ==========================================================
# FILTERS
# ==========================================================

c1,c2,c3,c4 = st.columns(4)

year = c1.selectbox(

    "Year",

    sorted(df["year"].unique()),

    index=len(df["year"].unique())-1

)

parameter = c2.selectbox(

    "Parameter",

    sorted(df["parameter"].dropna().unique())

)

mode = c3.selectbox(

    "Vehicle Type",

    ["All"] + sorted(df["mode"].dropna().unique())

)

powertrain = c4.selectbox(

    "Powertrain",

    ["All"] + sorted(df["powertrain"].dropna().unique())

)

filtered = df.copy()

filtered = filtered[
    filtered["year"]==year
]

filtered = filtered[
    filtered["parameter"]==parameter
]

if mode!="All":

    filtered = filtered[
        filtered["mode"]==mode
    ]

if powertrain!="All":

    filtered = filtered[
        filtered["powertrain"]==powertrain
    ]

st.success(f"{len(filtered):,} records selected")

st.divider()

# ==========================================================
# KPI ROW
# ==========================================================

k1,k2,k3,k4 = st.columns(4)

k1.metric(

    "Countries",

    filtered["region_country"].nunique()

)

k2.metric(

    "Average",

    f"{filtered['value'].mean():,.2f}"

)

k3.metric(

    "Maximum",

    f"{filtered['value'].max():,.0f}"

)

k4.metric(

    "Minimum",

    f"{filtered['value'].min():,.0f}"

)

st.divider()

# ==========================================================
# WORLD MAP
# ==========================================================

world = filtered.copy()

fig = px.choropleth(

    world,

    locations="region_country",

    locationmode="country names",

    color="value",

    hover_name="region_country",

    color_continuous_scale="Blues",

    title=f"{parameter} ({year})"

)

fig.update_layout(

    template="plotly_dark",

    paper_bgcolor="#0E1117",

    plot_bgcolor="#0E1117",

    height=600,

    coloraxis_colorbar_title=parameter

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# ==========================================================
# TOP COUNTRIES
# ==========================================================

top = (

    filtered

    .groupby("region_country")["value"]

    .sum()

    .nlargest(15)

    .reset_index()

)

fig = px.bar(

    top.sort_values("value"),

    x="value",

    y="region_country",

    orientation="h",

    text_auto=".2s",

    color="value",

    color_continuous_scale="Blues"

)

fig.update_layout(

    template="plotly_dark",

    paper_bgcolor="#0E1117",

    plot_bgcolor="#0E1117",

    height=650,

    title="Top 15 Countries"

)

fig.update_xaxes(showgrid=False)

fig.update_yaxes(showgrid=False)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# ==========================================================
# DISTRIBUTION
# ==========================================================

fig = px.box(

    filtered,

    x="mode",

    y="value",

    color="mode",

    points="outliers"

)

fig.update_layout(

    template="plotly_dark",

    paper_bgcolor="#0E1117",

    plot_bgcolor="#0E1117",

    title="Distribution by Vehicle Type"

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

    filtered,

    use_container_width=True,

    height=400

)