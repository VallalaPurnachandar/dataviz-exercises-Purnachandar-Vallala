# ==========================================================
# INFRASTRUCTURE & ENERGY ANALYSIS
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------

st.set_page_config(
    page_title="Infrastructure & Energy",
    page_icon="⚡",
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

st.title("⚡ Infrastructure & Energy")

st.markdown("""
Monitor charging infrastructure, electricity demand,
battery deployment and energy transition indicators.
""")

st.divider()

# ==========================================================
# FILTERS
# ==========================================================

c1,c2,c3 = st.columns(3)

parameter = c1.selectbox(

    "Infrastructure Parameter",

    [

        "EV charging points",

        "Electricity demand",

        "Battery deployment",

        "Oil displacement, Mbd"

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

category = c3.selectbox(
    "Scenario",
    sorted(
        df["category"]
        .dropna()
        .astype(str)
        .unique()
    )
)

infra = df[

    (df["parameter"]==parameter) &
    (df["region_country"]==country) &
    (df["category"]==category)

].copy()

# ==========================================================
# KPI CARDS
# ==========================================================

k1,k2,k3,k4 = st.columns(4)

k1.metric(

    "Years",

    infra["year"].nunique()

)

k2.metric(

    "Average",

    f"{infra['value'].mean():,.2f}"

)

k3.metric(

    "Maximum",

    f"{infra['value'].max():,.2f}"

)

k4.metric(

    "Latest",

    f"{infra.sort_values('year')['value'].iloc[-1]:,.2f}"

    if len(infra)>0 else "-"

)

st.divider()

# ==========================================================
# TREND CHART
# ==========================================================

st.subheader(parameter)

trend = (

    infra

    .groupby("year",as_index=False)["value"]

    .sum()

)

fig = px.area(

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

with left:

    st.subheader("Top Countries")

    top = (

        df[

            (df["parameter"]==parameter) &
            (df["category"]==category)

        ]

        .groupby("region_country",as_index=False)["value"]

        .sum()

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

        color_continuous_scale="Blues"

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

with right:

    st.subheader("Regional Distribution")

    region = (

        df[

            (df["parameter"]==parameter) &
            (df["category"]==category)

        ]

        .groupby("Aggregate group",as_index=False)["value"]

        .sum()

    )

    fig = px.pie(

        region,

        names="Aggregate group",

        values="value",

        hole=.55

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

st.divider()

# ==========================================================
# WORLD MAP
# ==========================================================

st.subheader("Global Infrastructure Distribution")

world = df[

    (df["parameter"]==parameter) &
    (df["category"]==category)

]

fig = px.choropleth(

    world,

    locations="region_country",

    locationmode="country names",

    color="value",

    hover_name="region_country",

    color_continuous_scale="Blues"

)

fig.update_layout(

    template="plotly_dark",

    paper_bgcolor="#0E1117",

    plot_bgcolor="#0E1117",

    height=600

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

    infra,

    use_container_width=True,

    height=350

)