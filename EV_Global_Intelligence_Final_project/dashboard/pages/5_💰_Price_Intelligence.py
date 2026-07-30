# ==========================================================
# PRICE INTELLIGENCE
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------

st.set_page_config(
    page_title="Price Intelligence",
    page_icon="💰",
    layout="wide"
)

# ----------------------------------------------------------
# LOAD DATA
# ----------------------------------------------------------

@st.cache_data
def load_data():

    project_dir = Path(__file__).resolve().parents[2]

    data_path = (
        project_dir /
        "data" /
        "processed" /
        "ev_analysis_ready.csv"
    )

    return pd.read_csv(data_path)

df = load_data()

# ==========================================================
# HEADER
# ==========================================================

st.title("💰 Price Intelligence")

st.markdown("""
Analyze EV prices across countries and understand pricing trends,
market differences, and affordability.
""")

st.divider()

# ==========================================================
# FILTERS
# ==========================================================

c1,c2,c3 = st.columns(3)

price_parameter = c1.selectbox(

    "Price Metric",

    [

        "price_mean_2025USD",

        "price_p25_2025USD",

        "price_p50_2025USD",

        "price_p75_2025USD",

        "price_p95_2025USD"

    ]

)

country = c2.selectbox(
    "Country",
    sorted(
        df["region_country"]
        .dropna()
        .astype(str)
        .unique()
    )
)

mode = c3.selectbox(
    "Vehicle Type",
    ["All"] + sorted(
        df["mode"]
        .dropna()
        .astype(str)
        .unique()
    )
)

price_df = df[
    (df["parameter"] == price_parameter) &
    (df["region_country"] == country)
].copy()

if mode != "All":
    price_df = price_df[
        price_df["mode"] == mode
    ]

# ==========================================================
# KPI CARDS
# ==========================================================

k1,k2,k3,k4 = st.columns(4)

k1.metric("Years", price_df["year"].nunique())

k2.metric(
    "Average Price",
    f"${price_df['value'].mean():,.0f}"
)

k3.metric(
    "Highest Price",
    f"${price_df['value'].max():,.0f}"
)

k4.metric(
    "Lowest Price",
    f"${price_df['value'].min():,.0f}"
)

st.divider()

# ==========================================================
# PRICE TREND
# ==========================================================

st.subheader("Price Trend")

trend = (
    price_df
    .groupby("year",as_index=False)["value"]
    .mean()
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
# TWO COLUMN LAYOUT
# ==========================================================

left,right = st.columns(2)

# ----------------------------------------------------------
# TOP COUNTRIES
# ----------------------------------------------------------

with left:

    st.subheader("Highest Average Prices")

    top = (

        df[
            df["parameter"] == price_parameter
        ]

        .groupby("region_country",as_index=False)["value"]

        .mean()

        .sort_values(
            "value",
            ascending=False
        )

        .head(10)

    )

    fig = px.bar(

        top,

        x="value",

        y="region_country",

        orientation="h",

        color="value",

        color_continuous_scale="Viridis"

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="#0E1117",

        plot_bgcolor="#0E1117",

        coloraxis_showscale=False

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------------------------------------
# PRICE DISTRIBUTION
# ----------------------------------------------------------

with right:

    st.subheader("Price Distribution")

    fig = px.box(

        price_df,

        x="powertrain",

        y="value",

        color="powertrain",

        points="outliers"

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
# COUNTRY HEATMAP
# ==========================================================

st.subheader("Country Price Comparison")

heat = (

    df[
        df["parameter"] == price_parameter
    ]

    .pivot_table(

        index="region_country",

        columns="year",

        values="value",

        aggfunc="mean"

    )

)

fig = px.imshow(

    heat,

    aspect="auto",

    color_continuous_scale="Viridis",

    text_auto=".0f"

)

fig.update_layout(

    template="plotly_dark",

    paper_bgcolor="#0E1117",

    plot_bgcolor="#0E1117",

    height=700

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

    price_df,

    use_container_width=True,

    height=350

)