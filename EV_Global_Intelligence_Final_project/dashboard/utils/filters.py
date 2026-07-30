"""
==========================================================
Dashboard Filters
Global EV Intelligence Dashboard
==========================================================
"""

import streamlit as st


# ==========================================================
# YEAR FILTER
# ==========================================================

def year_filter(df, label="Select Year"):

    years = sorted(df["year"].dropna().unique())

    return st.selectbox(
        label,
        years,
        index=len(years)-1
    )


# ==========================================================
# COUNTRY FILTER
# ==========================================================

def country_filter(df, label="Select Country", include_all=True):

    countries = sorted(df["region_country"].dropna().unique())

    if include_all:
        countries = ["All"] + countries

    return st.selectbox(label, countries)


# ==========================================================
# PARAMETER FILTER
# ==========================================================

def parameter_filter(df, label="Select Parameter"):

    parameters = sorted(
        df["parameter"].dropna().unique()
    )

    return st.selectbox(label, parameters)


# ==========================================================
# MODE FILTER
# ==========================================================

def mode_filter(df, label="Vehicle Type", include_all=True):

    modes = sorted(
        df["mode"].dropna().unique()
    )

    if include_all:
        modes = ["All"] + modes

    return st.selectbox(label, modes)


# ==========================================================
# POWERTRAIN FILTER
# ==========================================================

def powertrain_filter(
    df,
    label="Powertrain",
    include_all=True
):

    powertrains = sorted(
        df["powertrain"].dropna().unique()
    )

    if include_all:
        powertrains = ["All"] + powertrains

    return st.selectbox(
        label,
        powertrains
    )


# ==========================================================
# SCENARIO FILTER
# ==========================================================

def category_filter(
    df,
    label="Scenario",
    include_all=True
):

    categories = sorted(
        df["category"].dropna().unique()
    )

    if include_all:
        categories = ["All"] + categories

    return st.selectbox(
        label,
        categories
    )


# ==========================================================
# AGGREGATE GROUP FILTER
# ==========================================================

def aggregate_filter(
    df,
    label="Aggregate Group",
    include_all=True
):

    groups = sorted(
        df["Aggregate group"].dropna().unique()
    )

    if include_all:
        groups = ["All"] + groups

    return st.selectbox(
        label,
        groups
    )


# ==========================================================
# APPLY FILTERS
# ==========================================================

def apply_filters(
    df,
    year=None,
    country=None,
    parameter=None,
    mode=None,
    powertrain=None,
    category=None,
    aggregate_group=None
):

    filtered = df.copy()

    if year is not None:
        filtered = filtered[
            filtered["year"] == year
        ]

    if (
        country is not None
        and country != "All"
    ):
        filtered = filtered[
            filtered["region_country"] == country
        ]

    if (
        parameter is not None
    ):
        filtered = filtered[
            filtered["parameter"] == parameter
        ]

    if (
        mode is not None
        and mode != "All"
    ):
        filtered = filtered[
            filtered["mode"] == mode
        ]

    if (
        powertrain is not None
        and powertrain != "All"
    ):
        filtered = filtered[
            filtered["powertrain"] == powertrain
        ]

    if (
        category is not None
        and category != "All"
    ):
        filtered = filtered[
            filtered["category"] == category
        ]

    if (
        aggregate_group is not None
        and aggregate_group != "All"
    ):
        filtered = filtered[
            filtered["Aggregate group"] == aggregate_group
        ]

    return filtered


# ==========================================================
# FOUR COLUMN FILTER LAYOUT
# ==========================================================

def four_column_filters(df):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        year = year_filter(df)

    with c2:
        country = country_filter(df)

    with c3:
        parameter = parameter_filter(df)

    with c4:
        mode = mode_filter(df)

    return year, country, parameter, mode


# ==========================================================
# FIVE COLUMN FILTER LAYOUT
# ==========================================================

def five_column_filters(df):

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        year = year_filter(df)

    with c2:
        country = country_filter(df)

    with c3:
        parameter = parameter_filter(df)

    with c4:
        mode = mode_filter(df)

    with c5:
        powertrain = powertrain_filter(df)

    return (
        year,
        country,
        parameter,
        mode,
        powertrain
    )