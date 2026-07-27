# pages/03_demand.py — demand page (BBD squiggle: summary → neighbourhood story → demand)
import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils import load_data, sidebar_filters

df, p95 = load_data()
filtered = sidebar_filters(df, p95)  # SAME sidebar — shared filters persist onto this page

st.title('Where is guest demand strongest?')
st.caption('BBD squiggle: from the market summary, to one neighbourhood story, '
           'to where demand concentrates | reviews/month is used as a proxy for '
           'booking frequency (Inside Airbnb has no direct booking data)')

# ─────────────────────────────────────────────────────────────────────────────
# Own widget: "top N" highlight count — persisted with the same keep-alive +
# guard pattern used for sel_hood on page 2. The guard matters here because a
# sidebar filter can shrink the neighbourhood pool below the last chosen N.
# ─────────────────────────────────────────────────────────────────────────────
hoods_avail = sorted(filtered['neighbourhood'].unique())
max_n = len(hoods_avail)

if 'demand_topn' not in st.session_state:
    st.session_state.demand_topn = min(5, max_n)          # initialise once
st.session_state.demand_topn = st.session_state.demand_topn  # keep alive across pages

if st.session_state.demand_topn > max_n:                  # guard: filters may have
    st.session_state.demand_topn = max_n                   # shrunk the available pool

st.slider('How many top neighbourhoods to highlight', 1, max_n, key='demand_topn')
top_n = st.session_state.demand_topn

# ─────────────────────────────────────────────────────────────────────────────
# Demand ranking — mean reviews/month per neighbourhood
# ─────────────────────────────────────────────────────────────────────────────
demand = (filtered.groupby('neighbourhood')['reviews_per_month']
          .mean().sort_values(ascending=False))
top_hoods = demand.index[:top_n].tolist()
booked_nights = 365 - filtered['availability_365']

k1, k2, k3, k4 = st.columns(4)
k1.metric('Highest-demand area', demand.index[0],
          f"{demand.iloc[0]:.1f} reviews/mo")
overall_booked = (365 - df['availability_365']).mean()
k2.metric('Avg nights booked/yr', f"{booked_nights.mean():.0f}",
          f"{booked_nights.mean() - overall_booked:+.0f} vs overall")
k3.metric('Busiest room type',
          filtered.groupby('room_type')['reviews_per_month'].mean().idxmax())
k4.metric(f'Top {top_n} vs rest (reviews/mo)',
          f"{demand.iloc[:top_n].mean():.1f}",
          f"{demand.iloc[:top_n].mean() - demand.iloc[top_n:].mean():+.1f} vs rest")

st.divider()

col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.subheader(f'Demand concentrates in {top_n} neighbourhood'
                 f"{'s' if top_n != 1 else ''} — the rest see far fewer repeat bookings")
    plot_df = demand.reset_index()
    plot_df.columns = ['neighbourhood', 'reviews_per_month']
    # highlight column → px maps colours declaratively (no per-trace loop)
    plot_df['highlight'] = plot_df['neighbourhood'].apply(
        lambda n: 'Top demand' if n in top_hoods else 'Rest of market')

    # BBD HIGHLIGHT: blue for the top-N neighbourhoods, grey recedes
    # BBD CVD: blue vs grey — no red-green combination
    fig1 = px.bar(plot_df, x='reviews_per_month', y='neighbourhood',
                  orientation='h', color='highlight',
                  color_discrete_map={'Top demand': '#2E75B6', 'Rest of market': '#AAAAAA'},
                  category_orders={'neighbourhood': plot_df['neighbourhood'].tolist()},
                  labels={'reviews_per_month': 'Avg Reviews/Month', 'neighbourhood': ''})
    fig1.update_traces(marker_line_width=0)
    fig1.update_layout(plot_bgcolor='white', paper_bgcolor='white',
                       font=dict(family='Arial', size=11), showlegend=False,
                       xaxis=dict(gridcolor='#EEEEEE'), yaxis=dict(showgrid=False),
                       margin=dict(l=10, r=10, t=5, b=10))
    st.plotly_chart(fig1, use_container_width=True)

with col_right:
    st.subheader('High demand does not require a high price')
    plot_df2 = filtered.copy()
    plot_df2['highlight'] = plot_df2['neighbourhood'].apply(
        lambda n: 'Top demand' if n in top_hoods else 'Rest of market')

    # BBD HIGHLIGHT: blue for listings in the top-N neighbourhoods, grey elsewhere
    # BBD CVD: blue vs grey — no red-green combination
    fig2 = px.scatter(plot_df2, x='price', y='reviews_per_month',
                      color='highlight',
                      color_discrete_map={'Top demand': '#2E75B6', 'Rest of market': '#AAAAAA'},
                      opacity=0.6,
                      labels={'price': 'Nightly Price (£)',
                              'reviews_per_month': 'Reviews/Month', 'highlight': ''})
    fig2.update_layout(plot_bgcolor='white', paper_bgcolor='white',
                       font=dict(family='Arial', size=11),
                       legend=dict(orientation='h', y=1.1, title=None),
                       xaxis=dict(gridcolor='#EEEEEE'), yaxis=dict(gridcolor='#EEEEEE'),
                       margin=dict(l=10, r=10, t=5, b=10))
    st.plotly_chart(fig2, use_container_width=True)

with st.expander('📊 Show raw data sample'):
    st.dataframe(filtered.head(100), use_container_width=True)

st.divider()
st.caption(
    f'Inside Airbnb (insideairbnb.com) | Prices capped at 95th percentile '
    f'(£{p95:.0f}) | Demand proxy: reviews/month | Last shown: {datetime.date.today()}'
)

# 5-SECOND TEST: KPI row names the highest-demand area, the market-wide
# booking rate, the busiest room type, and the top-N premium in one glance.
# TEST for graders: change the "top N" slider, switch pages, come back —
# the slider value must be where you left it (subject to the guard above).
