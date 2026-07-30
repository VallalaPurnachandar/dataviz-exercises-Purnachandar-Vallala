"""
==========================================================
Plotly Chart Utilities
Global EV Intelligence Dashboard
==========================================================
"""

import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------------
# Global Theme
# ---------------------------------------------------------

PLOT_LAYOUT = dict(

    template="plotly_white",

    paper_bgcolor="white",

    plot_bgcolor="white",

    font=dict(color="#222222"),

    margin=dict(l=30,r=30,t=60,b=30),

    height=500
)

# =========================================================
# Line Chart
# =========================================================

def line_chart(
    df,
    x,
    y,
    title,
    color=None,
    markers=True
):

    fig = px.line(
        df,
        x=x,
        y=y,
        color=color,
        markers=markers
    )

    fig.update_layout(
        title=title,
        **PLOT_LAYOUT
    )

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    return fig


# =========================================================
# Bar Chart
# =========================================================

def bar_chart(
    df,
    x,
    y,
    title,
    color=None,
    orientation="v"
):

    fig = px.bar(
        df,
        x=x,
        y=y,
        color=color,
        orientation=orientation,
        text_auto=".2s"
    )

    fig.update_layout(
        title=title,
        showlegend=False,
        **PLOT_LAYOUT
    )

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    return fig


# =========================================================
# Pie Chart
# =========================================================

def pie_chart(
    df,
    names,
    values,
    title,
    hole=0.55
):

    fig = px.pie(
        df,
        names=names,
        values=values,
        hole=hole
    )

    fig.update_layout(
        title=title,
        **PLOT_LAYOUT
    )

    return fig


# =========================================================
# Area Chart
# =========================================================

def area_chart(
    df,
    x,
    y,
    title,
    color=None
):

    fig = px.area(
        df,
        x=x,
        y=y,
        color=color
    )

    fig.update_layout(
        title=title,
        **PLOT_LAYOUT
    )

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    return fig


# =========================================================
# Scatter Chart
# =========================================================

def scatter_chart(
    df,
    x,
    y,
    title,
    color=None,
    size=None
):

    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        size=size
    )

    fig.update_layout(
        title=title,
        **PLOT_LAYOUT
    )

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    return fig


# =========================================================
# Box Plot
# =========================================================

def box_chart(
    df,
    x,
    y,
    title,
    color=None
):

    fig = px.box(
        df,
        x=x,
        y=y,
        color=color,
        points="outliers"
    )

    fig.update_layout(
        title=title,
        **PLOT_LAYOUT
    )

    return fig


# =========================================================
# Heatmap
# =========================================================

def heatmap_chart(
    data,
    title
):

    fig = px.imshow(
        data,
        aspect="auto",
        text_auto=".2s",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        title=title,
        **PLOT_LAYOUT
    )

    return fig


# =========================================================
# Choropleth Map
# =========================================================

def choropleth_chart(
    df,
    locations,
    color,
    title,
    hover_name=None
):

    fig = px.choropleth(
        df,
        locations=locations,
        locationmode="country names",
        color=color,
        hover_name=hover_name,
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        title=title,
        **PLOT_LAYOUT
    )

    return fig


# =========================================================
# KPI Helper
# =========================================================

def format_number(value):

    if value >= 1_000_000_000:
        return f"{value/1_000_000_000:.2f} B"

    elif value >= 1_000_000:
        return f"{value/1_000_000:.2f} M"

    elif value >= 1_000:
        return f"{value/1_000:.2f} K"

    return f"{value:.2f}"