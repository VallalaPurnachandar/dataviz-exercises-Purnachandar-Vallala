# ==========================================================
# FUTURE OUTLOOK
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------

st.set_page_config(
    page_title="Future Outlook",
    page_icon="📈",
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

st.title("📈 Future Outlook")

st.markdown("""
Explore historical trends and future projections under different
IEA policy scenarios (Historical, Current Policies Scenario (CPS),
and Stated Policies Scenario (STEPS)).
""")

st.divider()

# ==========================================================
# FILTERS
# ==========================================================

c1, c2, c3 = st.columns(3)

parameter = c1.selectbox(
    "Forecast Parameter",
    sorted(df["parameter"].dropna().unique())
)

mode = c2.selectbox(
    "Vehicle Type",
    ["All"] + sorted(df["mode"].dropna().unique())
)

powertrain = c3.selectbox(
    "Powertrain",
    ["All"] + sorted(df["powertrain"].dropna().unique())
)

forecast_df = df[
    df["parameter"] == parameter
].copy()

if mode != "All":
    forecast_df = forecast_df[
        forecast_df["mode"] == mode
    ]

if powertrain != "All":
    forecast_df = forecast_df[
        forecast_df["powertrain"] == powertrain
    ]

forecast_df = forecast_df[
    forecast_df["Aggregate group"] == "_World"
]

# ==========================================================
# KPI CARDS
# ==========================================================

hist = forecast_df[
    forecast_df["category"] == "Historical"
]

cps = forecast_df[
    forecast_df["category"] == "Projection-CPS"
]

steps = forecast_df[
    forecast_df["category"] == "Projection-STEPS"
]

k1, k2, k3, k4 = st.columns(4)

latest_hist = hist.sort_values("year")["value"].iloc[-1] if len(hist) else 0
latest_cps = cps["value"].max() if len(cps) else 0
latest_steps = steps["value"].max() if len(steps) else 0

k1.metric("Historical", f"{latest_hist:,.0f}")
k2.metric("CPS (2035)", f"{latest_cps:,.0f}")
k3.metric("STEPS (2035)", f"{latest_steps:,.0f}")

if latest_cps > 0:
    growth = ((latest_steps-latest_cps)/latest_cps)*100
else:
    growth = 0

k4.metric("Policy Difference", f"{growth:.1f}%")

st.divider()

# ==========================================================
# FORECAST TREND
# ==========================================================

st.subheader("Historical vs Future Projection")

trend = (
    forecast_df
    .groupby(["year","category"],as_index=False)["value"]
    .sum()
)

fig = px.line(
    trend,
    x="year",
    y="value",
    color="category",
    markers=True,
    color_discrete_map={
        "Historical":"#2F81F7",
        "Projection-CPS":"#F39C12",
        "Projection-STEPS":"#2ECC71"
    }
)

fig.add_vline(
    x=2025,
    line_dash="dash",
    line_color="white"
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    height=550,
    title="Historical Performance and Future Scenarios"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# TWO COLUMN ANALYSIS
# ==========================================================

left, right = st.columns(2)

with left:

    st.subheader("Scenario Comparison")

    compare = forecast_df[
        forecast_df["category"] != "Historical"
    ]

    compare = (
        compare
        .groupby("category", as_index=False)["value"]
        .max()
    )

    fig = px.bar(
        compare,
        x="category",
        y="value",
        color="category",
        text_auto=".2s",
        color_discrete_map={
            "Projection-CPS":"#F39C12",
            "Projection-STEPS":"#2ECC71"
        }
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

with right:

    st.subheader("Projection Distribution")

    fig = px.box(
        forecast_df[
            forecast_df["category"] != "Historical"
        ],
        x="category",
        y="value",
        color="category"
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
# TOP PROJECTED COUNTRIES
# ==========================================================

st.subheader("Top Projected Countries")

future = df[
    (df["parameter"] == parameter) &
    (df["category"] == "Projection-STEPS") &
    (df["Aggregate group"] == "Projection_country")
]

top = (
    future
    .groupby("region_country", as_index=False)["value"]
    .sum()
    .sort_values("value", ascending=False)
    .head(10)
)

fig = px.bar(
    top.sort_values("value"),
    x="value",
    y="region_country",
    orientation="h",
    color="value",
    color_continuous_scale="Greens"
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    coloraxis_showscale=False,
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# STRATEGIC INSIGHTS
# ==========================================================

st.subheader("Strategic Insights")

st.success(f"""
### Key Findings

- Historical trends show continuous growth in **{parameter}**.
- Under the **STEPS** scenario, future values exceed the **Current Policies Scenario (CPS)**.
- Stronger policy implementation accelerates market development.
- Countries leading the projection are expected to require greater investment in infrastructure and supporting technologies.
- Long-term planning should align transportation, energy, and industrial policies to support sustained EV market growth.
""")

st.divider()

# ==========================================================
# DATA TABLE
# ==========================================================

st.subheader("Forecast Dataset")

st.dataframe(
    forecast_df,
    use_container_width=True,
    height=350
)