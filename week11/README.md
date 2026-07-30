# Gapminder Multi-Page Dashboard

A 3-page Streamlit dashboard built on the BBD "squiggle" principle: each page
answers a question, and answering it raises the next one — **summary → pattern → detail**.

## Pages

| Page | Question | Granularity |
|---|---|---|
| `pages/01_overview.py` | How do countries compare today? | Summary snapshot |
| `pages/02_trends.py` | How does wealth relate to emissions? | Pattern across GDP tiers |
| `pages/03_compare.py` | What explains the differences? | Individual country drill-down |

## Data note

`data/gapminder.csv` is a **single-year snapshot** (47 countries, no `year`
column) — it's not the multi-year `px.data.gapminder()` dataset used in the
lecture demo. Because there's no time axis, Page 2 shows the trend *across
GDP-per-capita tiers* (Low → High income quartiles) instead of a trend over
time. Same squiggle logic — an ordered variable other than time.

## Project structure

```
week11/
  app.py                  # entry point, defines navigation
  utils.py                # @st.cache_data data loading, shared across pages
  data/
    gapminder.csv
  pages/
    01_overview.py
    02_trends.py
    03_compare.py
  requirements.txt
```

## Setup & run

```bash
cd week11
pip install -r requirements.txt
streamlit run app.py
```

The app opens at `http://localhost:8501`. Use the sidebar nav to move between
the three pages.

## Features used

- **`@st.cache_data`** in `utils.py` — the same cached DataFrame is reused
  across all pages instead of re-reading the CSV on every page visit.
- **`st.session_state`** in `pages/03_compare.py` — the highlighted country
  selection persists across reruns and across tabs.
- **`st.tabs()`** in `pages/03_compare.py` — switches between "GDP vs Life
  Expectancy" and "Continent comparison" views without leaving the page.
- **Categorical color encoding** — continent is used as an unordered
  categorical color channel throughout (noted in a comment on each chart).
- **Highlight color encoding** — Page 3 uses one bold color for the selected
  country and grey for all others (BBD/SWD highlight technique).

## Requirements

```
streamlit
pandas
plotly
```
Deployed Streamlit app:
https://dataviz-exercises-purnachandar-vallala-bjmoy4klmnecchzh8cabxh.streamlit.app/
