"""
==========================================================
Global EV Intelligence Dashboard
Home Dashboard
==========================================================
"""

# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from utils.loader import load_dataset
from utils.styles import apply_styles
from utils.charts import format_number

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Global EV Intelligence Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# Apply Dashboard Theme
# ==========================================================

apply_styles()

# ==========================================================
# Load Dataset
# ==========================================================

df = load_dataset()

# ==========================================================
# Sidebar Logo
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[1]

logo_path = BASE_DIR / "images" / "logo.png"

st.sidebar.image(
    logo_path,
    width=90
)


st.sidebar.title("Global EV")

st.sidebar.caption(
    "Business Intelligence Dashboard"
)

st.sidebar.markdown("---")

st.sidebar.success(
    "Interactive dashboard for analysing the global EV market between 2010 and 2035."
)

st.sidebar.markdown("---")

st.sidebar.markdown(
"""
### Dashboard Sections

- 📊 Market Overview
- 🌍 Country Explorer
- 🚗 Vehicle Technology
- ⚡ Infrastructure & Energy
- 💰 Price Intelligence
- 📈 Future Outlook
- 💼 Executive Insights
"""
)

# ==========================================================
# Dashboard Title
# ==========================================================

st.title("⚡ Global EV Intelligence Dashboard")

st.markdown(
"""
### Interactive Business Intelligence Platform

Explore the global electric vehicle market using interactive
visualizations, executive KPIs and forecasting insights.

**Coverage:** 72 Countries • 2010–2035 • Historical + Forecast Scenarios
"""
)

st.divider()
# ==========================================================
# Executive KPI Calculations
# ==========================================================

# -----------------------------
# Global EV Sales (2025)
# -----------------------------

sales_df = df[
    (df["parameter"] == "EV sales") &
    (df["Aggregate group"] == "_World") &
    (df["mode"] == "Cars") &
    (df["powertrain"] == "EV") &
    (df["year"] == 2025)
]

sales_2025 = sales_df["value"].sum() if not sales_df.empty else 0

# -----------------------------
# Global EV Stock (2025)
# -----------------------------

stock_df = df[
    (df["parameter"] == "EV stock") &
    (df["Aggregate group"] == "_World") &
    (df["mode"] == "Cars") &
    (df["powertrain"] == "EV") &
    (df["year"] == 2025)
]

stock_2025 = stock_df["value"].sum() if not stock_df.empty else 0

# -----------------------------
# Charging Points (2025)
# -----------------------------

charging_df = df[
    (df["parameter"] == "EV charging points") &
    (df["year"] == 2025)
]

charging_points = charging_df["value"].sum() if not charging_df.empty else 0

# -----------------------------
# Average EV Price (2025)
# -----------------------------

price_df = df[
    (df["parameter"] == "price_mean_2025USD") &
    (df["year"] == 2025)
]

average_price = price_df["value"].mean() if not price_df.empty else 0

# -----------------------------
# Countries
# -----------------------------

countries = df["region_country"].dropna().nunique()

# ==========================================================
# Executive KPI Dashboard
# ==========================================================

st.subheader("📊 Executive Dashboard")

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

with kpi1:

    st.metric(
        label="🚗 EV Sales",
        value=format_number(sales_2025)
    )

with kpi2:

    st.metric(
        label="⚡ EV Stock",
        value=format_number(stock_2025)
    )

with kpi3:

    st.metric(
        label="🔌 Charging Points",
        value=format_number(charging_points)
    )

with kpi4:

    st.metric(
        label="🌍 Countries",
        value=countries
    )

with kpi5:

    st.metric(
        label="💰 Avg EV Price",
        value=f"${average_price:,.0f}"
    )

st.divider()
# ==========================================================
# GLOBAL EV SALES TREND
# ==========================================================

st.subheader("📈 Global EV Sales Outlook (2010–2035)")

hero = df[
    (df["parameter"] == "EV sales") &
    (df["mode"] == "Cars") &
    (df["powertrain"] == "EV") &
    (df["Aggregate group"] == "_World")
].sort_values("year")

historical = hero[
    hero["category"] == "Historical"
]

cps = hero[
    hero["category"] == "Projection-CPS"
]

steps = hero[
    hero["category"] == "Projection-STEPS"
]

# ==========================================================
# Build Figure
# ==========================================================

fig = go.Figure()

# ----------------------------------------------------------
# Historical
# ----------------------------------------------------------

fig.add_trace(

    go.Scatter(

        x=historical["year"],

        y=historical["value"],

        mode="lines+markers",

        name="Historical",

        line=dict(
            color="#2563EB",
            width=4
        ),

        marker=dict(
            size=7
        )

    )

)

# ----------------------------------------------------------
# CPS
# ----------------------------------------------------------

fig.add_trace(

    go.Scatter(

        x=cps["year"],

        y=cps["value"],

        mode="markers",

        name="Projection - CPS",

        marker=dict(
            color="#F59E0B",
            size=14,
            symbol="diamond"
        )

    )

)

# ----------------------------------------------------------
# STEPS
# ----------------------------------------------------------

fig.add_trace(

    go.Scatter(

        x=steps["year"],

        y=steps["value"],

        mode="markers",

        name="Projection - STEPS",

        marker=dict(
            color="#10B981",
            size=14,
            symbol="diamond"
        )

    )

)

# ----------------------------------------------------------
# Forecast Divider
# ----------------------------------------------------------

fig.add_vline(

    x=2025,

    line_dash="dash",

    line_color="gray"

)

fig.add_annotation(

    x=2025,

    y=historical["value"].max(),

    text="Forecast Begins",

    showarrow=False,

    yshift=30,

    font=dict(
        size=12,
        color="#555555"
    )

)

# ----------------------------------------------------------
# Layout
# ----------------------------------------------------------

fig.update_layout(

    template="plotly_white",

    title="Global Passenger EV Sales Continue to Grow Through 2035",

    height=600,

    hovermode="x unified",

    paper_bgcolor="white",

    plot_bgcolor="white",

    legend=dict(

        orientation="h",

        y=1.05,

        x=0

    ),

    margin=dict(

        l=20,

        r=20,

        t=70,

        b=20

    )

)

fig.update_xaxes(

    title="Year",

    showgrid=False

)

fig.update_yaxes(

    title="EV Sales",

    showgrid=True,

    gridcolor="#EEEEEE"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()
# ==========================================================
# EXECUTIVE INSIGHTS
# ==========================================================

left_col, right_col = st.columns(2)

# ==========================================================
# LEFT PANEL
# Vehicle Distribution
# ==========================================================

with left_col:

    st.subheader("🚗 EV Sales by Vehicle Segment (2025)")

    vehicle_df = (

        df[
            (df["parameter"] == "EV sales") &
            (df["year"] == 2025) &
            (df["category"] == "Historical") &
            (df["Aggregate group"] == "_World")
        ]

        .groupby("mode", as_index=False)["value"]

        .sum()

    )

    fig_vehicle = px.pie(

        vehicle_df,

        names="mode",

        values="value",

        hole=0.60,

        color_discrete_sequence=px.colors.qualitative.Set2

    )

    fig_vehicle.update_traces(

        textposition="inside",

        textinfo="percent+label",

        hovertemplate="<b>%{label}</b><br>%{value:,.0f}<extra></extra>"

    )

    fig_vehicle.update_layout(

        template="plotly_white",

        paper_bgcolor="white",

        plot_bgcolor="white",

        height=450,

        showlegend=False,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )

    )

    st.plotly_chart(
        fig_vehicle,
        use_container_width=True
    )

# ==========================================================
# RIGHT PANEL
# Top EV Markets
# ==========================================================

with right_col:

    st.subheader("🌍 Top 10 EV Markets (2025)")

    top_df = (

        df[
            (df["parameter"] == "EV stock") &
            (df["mode"] == "Cars") &
            (df["powertrain"] == "EV") &
            (df["category"] == "Historical") &
            (df["year"] == 2025)
        ]

        .groupby("region_country", as_index=False)["value"]

        .sum()

        .sort_values(
            "value",
            ascending=False
        )

        .head(10)

    )

    fig_country = px.bar(

        top_df.sort_values("value"),

        x="value",

        y="region_country",

        orientation="h",

        color="value",

        text_auto=".2s",

        color_continuous_scale="Blues"

    )

    fig_country.update_layout(

        template="plotly_white",

        paper_bgcolor="white",

        plot_bgcolor="white",

        height=450,

        coloraxis_showscale=False,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )

    )

    fig_country.update_xaxes(
        title="EV Stock",
        showgrid=False
    )

    fig_country.update_yaxes(
        title="",
        showgrid=False
    )

    st.plotly_chart(
        fig_country,
        use_container_width=True
    )

st.divider()
# ==========================================================
# INTERACTIVE DATA EXPLORER
# ==========================================================

st.subheader("🔎 Explore the Dataset")

col1, col2, col3, col4 = st.columns(4)

# -----------------------------
# Filters
# -----------------------------

with col1:

    selected_year = st.selectbox(
        "Year",
        sorted(df["year"].dropna().unique()),
        index=len(sorted(df["year"].dropna().unique()))-1
    )

with col2:

    country_list = ["All"] + sorted(
        df["region_country"]
        .dropna()
        .astype(str)
        .unique()
    )

    selected_country = st.selectbox(
        "Country",
        country_list
    )

with col3:

    mode_list = ["All"] + sorted(
        df["mode"]
        .dropna()
        .astype(str)
        .unique()
    )

    selected_mode = st.selectbox(
        "Vehicle Type",
        mode_list
    )

with col4:

    parameter_list = sorted(
        df["parameter"]
        .dropna()
        .astype(str)
        .unique()
    )

    selected_parameter = st.selectbox(
        "Parameter",
        parameter_list
    )

# ==========================================================
# APPLY FILTERS
# ==========================================================

filtered_df = df.copy()

filtered_df = filtered_df[
    filtered_df["year"] == selected_year
]

filtered_df = filtered_df[
    filtered_df["parameter"] == selected_parameter
]

if selected_country != "All":

    filtered_df = filtered_df[
        filtered_df["region_country"] == selected_country
    ]

if selected_mode != "All":

    filtered_df = filtered_df[
        filtered_df["mode"] == selected_mode
    ]

# ==========================================================
# FILTER SUMMARY
# ==========================================================

st.markdown("### 📌 Filter Summary")

summary1, summary2, summary3 = st.columns(3)

with summary1:

    st.metric(
        "Matching Records",
        len(filtered_df)
    )

with summary2:

    st.metric(
        "Countries",
        filtered_df["region_country"].nunique()
    )

with summary3:

    if not filtered_df.empty:

        st.metric(
            "Average Value",
            f"{filtered_df['value'].mean():,.2f}"
        )

    else:

        st.metric(
            "Average Value",
            "N/A"
        )

st.divider()

# ==========================================================
# FILTERED DATA
# ==========================================================

st.subheader("📄 Filtered Dataset")

st.dataframe(

    filtered_df,

    use_container_width=True,

    height=350

)

# ==========================================================
# DOWNLOAD DATA
# ==========================================================

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(

    label="⬇ Download Filtered Data",

    data=csv,

    file_name="filtered_ev_data.csv",

    mime="text/csv"

)

st.divider()

# ==========================================================
# EXECUTIVE INSIGHTS
# ==========================================================

st.subheader("💼 Executive Insights")

col1, col2 = st.columns(2)

# ----------------------------------------------------------
# Key Findings
# ----------------------------------------------------------

with col1:

    st.info("""
### 📌 Key Business Findings

- Global EV adoption has accelerated significantly since 2015.

- Passenger cars dominate worldwide EV sales.

- China, Europe and the United States continue to lead the global EV market.

- Public charging infrastructure has expanded rapidly to support market growth.

- Under the IEA STEPS scenario, EV adoption is expected to continue growing strongly through 2035.

- Falling battery costs continue to improve EV affordability.

""")

# ----------------------------------------------------------
# Strategic Recommendations
# ----------------------------------------------------------

with col2:

    st.success("""
### 🚀 Strategic Recommendations

- Continue investing in public charging infrastructure.

- Support battery manufacturing and recycling.

- Promote affordable EV models for wider adoption.

- Expand renewable energy integration with transport electrification.

- Encourage policy incentives to accelerate market transition.

- Strengthen international collaboration across the EV supply chain.

""")

st.divider()

# ==========================================================
# ABOUT THE PROJECT
# ==========================================================

st.subheader("📚 About this Dashboard")

st.markdown("""

The **Global EV Intelligence Dashboard** provides an interactive business
intelligence platform for analysing the worldwide electric vehicle market.

The dashboard integrates:

- Historical EV market performance
- Country-level comparisons
- Vehicle technology analysis
- Charging infrastructure
- Electricity demand
- EV price intelligence
- Future market projections
- Executive business insights

The analysis is based on the **International Energy Agency (IEA) Global EV Outlook** dataset covering **2010–2035**.

""")

st.divider()

# ==========================================================
# PROJECT STATISTICS
# ==========================================================

st.subheader("📊 Dashboard Summary")

summary1, summary2, summary3, summary4 = st.columns(4)

summary1.metric(
    "Countries",
    df["region_country"].nunique()
)

summary2.metric(
    "Years",
    f"{df['year'].min()}–{df['year'].max()}"
)

summary3.metric(
    "Parameters",
    df["parameter"].nunique()
)

summary4.metric(
    "Records",
    f"{len(df):,}"
)

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
"""
---
<div style='text-align:center; color:gray;'>

### Global EV Intelligence Dashboard

Business Intelligence & Interactive Analytics Platform

Developed using **Python • Streamlit • Plotly • Pandas**

**Author:** Purnachandar Vallala

Master's in Data Science

2026

</div>
""",
unsafe_allow_html=True
)