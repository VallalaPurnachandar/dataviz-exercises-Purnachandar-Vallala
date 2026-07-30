# ==========================================================
# VEHICLE & TECHNOLOGY ANALYSIS
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------

st.set_page_config(
    page_title="Vehicle & Technology Analysis",
    page_icon="🚗",
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

st.title("🚗 Vehicle & Technology Analysis")

st.markdown("""
Compare electric vehicle adoption across vehicle segments and powertrain technologies.
""")

st.divider()

# ==========================================================
# FILTERS
# ==========================================================

c1,c2,c3 = st.columns(3)

year = c1.selectbox(
    "Year",
    sorted(df["year"].unique()),
    index=len(df["year"].unique())-1
)

parameter = c2.selectbox(
    "Parameter",
    sorted(df["parameter"].dropna().unique())
)

category = c3.selectbox(
    "Scenario",
    sorted(df["category"].dropna().unique())
)

vehicle_df = df[
    (df["year"]==year) &
    (df["parameter"]==parameter) &
    (df["category"]==category)
]

# ==========================================================
# KPI CARDS
# ==========================================================

k1,k2,k3,k4 = st.columns(4)

k1.metric(
    "Vehicle Types",
    vehicle_df["mode"].nunique()
)

k2.metric(
    "Powertrains",
    vehicle_df["powertrain"].nunique()
)

k3.metric(
    "Countries",
    vehicle_df["region_country"].nunique()
)

k4.metric(
    "Records",
    len(vehicle_df)
)

st.divider()

# ==========================================================
# VEHICLE SEGMENT BAR CHART
# ==========================================================

st.subheader("Vehicle Segment Comparison")

segment = (
    vehicle_df
    .groupby("mode",as_index=False)["value"]
    .sum()
)

fig = px.bar(
    segment,
    x="mode",
    y="value",
    color="mode",
    text_auto=".2s"
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    height=500,
    showlegend=False
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

with left:

    st.subheader("Powertrain Share")

    power = (
        vehicle_df
        .groupby("powertrain",as_index=False)["value"]
        .sum()
    )

    fig = px.pie(
        power,
        names="powertrain",
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

# ----------------------------------------------------------

with right:

    st.subheader("Vehicle Segment Heatmap")

    heat = (
        vehicle_df
        .pivot_table(
            index="mode",
            columns="powertrain",
            values="value",
            aggfunc="sum"
        )
        .fillna(0)
    )

    fig = px.imshow(
        heat,
        text_auto=".2s",
        aspect="auto",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#0E1117",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================================================
# TREND ANALYSIS
# ==========================================================

st.subheader("Historical Trend")

mode_selected = st.selectbox(
    "Select Vehicle Type",
    sorted(df["mode"].dropna().unique())
)

trend = df[
    (df["mode"]==mode_selected) &
    (df["parameter"]==parameter)
]

trend = (
    trend
    .groupby("year",as_index=False)["value"]
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

st.divider()

# ==========================================================
# DATA TABLE
# ==========================================================

st.subheader("Filtered Dataset")

st.dataframe(
    vehicle_df,
    use_container_width=True,
    height=400
)