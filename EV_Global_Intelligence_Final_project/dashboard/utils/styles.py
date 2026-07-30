"""
==========================================================
Dashboard Styles
Global EV Intelligence Dashboard
Light Theme
==========================================================
"""

import streamlit as st


def apply_styles():

    st.markdown(
        """
        <style>

        /* ======================================================
           MAIN APP
        ====================================================== */

        .stApp{
            background:#FFFFFF;
        }

        [data-testid="stAppViewContainer"]{
            background:#FFFFFF;
        }

        .block-container{
            max-width:1450px;
            padding-top:1rem;
            padding-bottom:1rem;
        }

        /* ======================================================
           HEADER
        ====================================================== */

        [data-testid="stHeader"]{
            background:rgba(255,255,255,0);
        }

        /* ======================================================
           SIDEBAR
        ====================================================== */

        [data-testid="stSidebar"]{

            background:#F8F9FA;

            border-right:1px solid #E5E7EB;

        }

        [data-testid="stSidebar"] *{

            color:#222222;

        }

        /* ======================================================
           TITLES
        ====================================================== */

        h1{
            color:#222222;
            font-size:2.2rem;
            font-weight:700;
        }

        h2{
            color:#222222;
            font-weight:700;
        }

        h3{
            color:#222222;
            font-weight:600;
        }

        h4{
            color:#222222;
        }

        p{

            color:#555555;

        }

        /* ======================================================
           METRIC CARDS
        ====================================================== */

        div[data-testid="metric-container"]{

            background:white;

            border:1px solid #E5E7EB;

            padding:18px;

            border-radius:14px;

            box-shadow:
            0px 2px 10px rgba(0,0,0,0.08);

            transition:0.25s;

        }

        div[data-testid="metric-container"]:hover{

            border:1px solid #2563EB;

            transform:translateY(-3px);

        }

        /* ======================================================
           BUTTONS
        ====================================================== */

        .stButton>button{

            background:#2563EB;

            color:white;

            border:none;

            border-radius:8px;

            font-weight:600;

        }

        .stButton>button:hover{

            background:#1D4ED8;

            color:white;

        }

        /* ======================================================
           DOWNLOAD BUTTON
        ====================================================== */

        .stDownloadButton>button{

            background:#16A34A;

            color:white;

            border:none;

            border-radius:8px;

        }

        /* ======================================================
           SELECT BOXES
        ====================================================== */

        .stSelectbox{

            color:#222222;

        }

        /* ======================================================
           DATAFRAMES
        ====================================================== */

        .stDataFrame{

            border:1px solid #E5E7EB;

            border-radius:10px;

        }

        /* ======================================================
           EXPANDERS
        ====================================================== */

        .streamlit-expanderHeader{

            font-size:16px;

            font-weight:600;

            color:#222222;

        }

        /* ======================================================
           TABS
        ====================================================== */

        button[data-baseweb="tab"]{

            font-size:16px;

            color:#222222;

        }

        /* ======================================================
           INFO / SUCCESS / WARNING
        ====================================================== */

        div[data-baseweb="notification"]{

            border-radius:12px;

        }

        /* ======================================================
           HORIZONTAL RULE
        ====================================================== */

        hr{

            border:1px solid #ECECEC;

        }

        /* ======================================================
           SCROLLBAR
        ====================================================== */

        ::-webkit-scrollbar{

            width:10px;

        }

        ::-webkit-scrollbar-thumb{

            background:#CFCFCF;

            border-radius:10px;

        }

        ::-webkit-scrollbar-thumb:hover{

            background:#9CA3AF;

        }

        /* ======================================================
           PLOTLY
        ====================================================== */

        .js-plotly-plot{

            border-radius:12px;

        }

        /* ======================================================
           HIDE STREAMLIT
        ====================================================== */

        #MainMenu{

            visibility:hidden;

        }

        footer{

            visibility:hidden;

        }

        header{

            visibility:hidden;

        }

        </style>
        """,
        unsafe_allow_html=True
    )