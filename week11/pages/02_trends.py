import os
import sys

import pandas as pd
import plotly.express as px
import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils import load_gapminder

df = load_gapminder()
st.header("How does wealth relate to emissions?")
st.caption(
    "This gapminder.csv is a single-year snapshot (no year column), so instead of a "
    "time trend we show the *trend across income levels* — grouping countries into "
    "GDP-per-capita tiers to reveal the pattern the squiggle asks about next."
)

with st.sidebar:
    st.header("Filters")
    continents = st.multiselect(
        "Continent", df["Continent"].unique(), default=list(df["Continent"].unique())
    )
    metric = st.radio("Metric", ["CO2 per Capita", "Life Expectancy"])

if not continents:
    st.warning("Select at least one continent.")
    st.stop()

y_col = "CO2_per_capita" if metric == "CO2 per Capita" else "Life_expectancy"

df_f = df[df["Continent"].isin(continents)].copy()
df_f["GDP tier"] = pd.qcut(
    df_f["GDP_per_capita"], q=4, labels=["Low", "Lower-mid", "Upper-mid", "High"]
)

avg = df_f.groupby(["Continent", "GDP tier"], observed=True)[y_col].mean().reset_index()

# BBD CATEGORICAL: distinct hue per continent (unordered groups)
fig = px.line(
    avg, x="GDP tier", y=y_col, color="Continent", markers=True,
    labels={y_col: metric, "GDP tier": "GDP per Capita Tier"},
    title=f"{metric} rises with income — richer tiers pull further ahead",
)
fig.update_layout(
    plot_bgcolor="white", paper_bgcolor="white", font=dict(family="Arial", size=12),
    yaxis=dict(gridcolor="#EEEEEE"), xaxis=dict(showgrid=False),
    legend=dict(orientation="h", y=1.08),
)
st.plotly_chart(fig, use_container_width=True)
