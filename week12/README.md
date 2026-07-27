# London Airbnb Analytics

A multi-page Streamlit dashboard analysing Airbnb listings in London, built for
Lecture 12 — Dashboard Design & Polish. The app follows a "squiggle" narrative
structure: market overview → neighbourhood drill-down → guest demand.

## Live structure

| Page | Question it answers | Icon |
|---|---|---|
| `pages/01_market.py` | Is London Airbnb expensive right now? | 🏠 |
| `pages/02_drilldown.py` | Which neighbourhoods drive the premium? | 📍 |
| `pages/03_demand.py` | Where is guest demand strongest? | 🔥 |

Filters set in the sidebar (room type, neighbourhood, price range) are shared
across all three pages and persist as you navigate between them.

## Project layout

```
week12/
├── app.py                  # Entry point: page config + navigation
├── utils.py                # Cached data loader + shared sidebar filters
├── requirements.txt
├── data/
│   └── airbnb_london.csv
└── pages/
    ├── 01_market.py         # Market summary (KPIs, price by area, room type mix)
    ├── 02_drilldown.py      # Neighbourhood drill-down vs. filtered market
    └── 03_demand.py         # Demand ranking + price-vs-demand scatter
```

## Getting started

```bash
# 1. Create and activate a virtual environment (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app (from the week12/ directory)
streamlit run app.py
```

The app opens at `http://localhost:8501`.

## Data

`data/airbnb_london.csv` (2,500 listings) with the following columns:

| Column | Description |
|---|---|
| `neighbourhood` | London borough |
| `room_type` | Entire home/apt, Private room, or Shared room |
| `price` | Nightly price in £ |
| `minimum_nights` | Minimum stay required |
| `number_of_reviews` | Total reviews to date |
| `availability_365` | Days available in the next year |
| `reviews_per_month` | Average reviews per month — used throughout as a proxy for booking demand, since Inside Airbnb does not publish actual booking data |

Source: [Inside Airbnb](http://insideairbnb.com/). Prices are capped at the
95th percentile inside `load_data()` so a small number of extreme outliers
don't distort the charts.

## Design principles applied (Big Book of Dashboards)

- **No red/green as the only differentiator** — every highlight uses
  blue (`#2E75B6`) and orange (`#E07B39`) against grey (`#AAAAAA`), which
  remains distinguishable for colour-vision-deficient viewers.
- **No pies, donuts, or packed bubbles.**
- **5-second test** — every page opens with a KPI row stating the single
  most important numbers before any chart is read.
- **Insight titles, not topic titles** — chart subheaders state the finding
  (e.g. *"Demand concentrates in 5 neighbourhoods"*) rather than a generic
  label like "Reviews by Area".
- **Progressive disclosure** — raw data is tucked into a collapsed
  `st.expander` on every page.
- **Data freshness footer** — every page states its data source and the
  date last shown.

## Filter & state persistence

Streamlit reruns each page as an independent script and deletes the
`session_state` key of any widget that isn't rendered in the current run. To
keep filters and selections alive across page switches, this app uses the
"keep-alive" pattern throughout:

```python
if key not in st.session_state:
    st.session_state[key] = default_value      # initialise once
else:
    st.session_state[key] = st.session_state[key]   # re-assign every run
```

This is centralised in `utils.py` (`init_filters` / `sidebar_filters`) for the
sidebar filters, and repeated locally for each page's own widget:

- Page 2's neighbourhood drill-down selector (`sel_hood`)
- Page 3's "top N neighbourhoods to highlight" slider (`demand_topn`)

Both include a **guard**: if the sidebar filters shrink the pool of available
neighbourhoods, the saved selection/value is clamped back into range instead
of throwing an error.

**Manual test:** set filters and a selection on any page, switch to another
page, then switch back — both the shared filters and the page-specific
selection should be exactly where you left them.

## Requirements

See `requirements.txt`:

```
streamlit>=1.36.0
pandas>=2.0.0
plotly>=5.20.0
```

`streamlit>=1.36.0` is required for `st.navigation` / `st.Page`, which power
the multi-page structure in `app.py`.
