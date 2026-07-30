from pathlib import Path
import pandas as pd
import streamlit as st


@st.cache_data
def load_dataset():

    project_dir = Path(__file__).resolve().parents[2]

    data_path = (
        project_dir
        / "data"
        / "processed"
        / "ev_analysis_ready.csv"
    )

    df = pd.read_csv(data_path)

    return df