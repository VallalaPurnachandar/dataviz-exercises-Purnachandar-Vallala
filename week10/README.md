# 🌱 CO2 Emissions Explorer

An interactive Streamlit dashboard for exploring global CO2 emissions trends by country and region, built as a data visualization exercise applying **Storytelling with Data (SWD)** and **Big Book of Dashboards (BBD)** design principles.

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.3x-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Overview

This dashboard lets users filter and compare CO2 emissions across 15 countries and 6 regions from 2000–2022, using data from [Our World in Data](https://ourworldindata.org/co2-emissions). It supports two metrics — total emissions (Mt) and per-capita emissions — and applies deliberate color and layout choices to make the underlying trends easy to read at a glance.

## Features

- **Chained filters** — Region selection narrows the available country list; countries, date range, and metric can all be adjusted independently
- **Filter summary caption** — always shows the number of matching records, following the BBD principle that users should never be left guessing how much data they're looking at
- **KPI row** — total emissions in the latest year, percent change over the selected period, and the top emitter, all recalculated live from the current filter state
- **Line chart** — emissions over time, one line per country, with an optional "highlight top emitter" mode that mutes all other lines to grey and labels the leading country directly on the chart (SWD grey-and-highlight technique)
- **Bar chart** — ranks countries by the selected metric in the most recent year of the selected range
- **Guardrails** — clear warnings (rather than crashes) when no countries are selected or the date range is incomplete

## Screenshots

<img width="918" height="476" alt="image" src="https://github.com/user-attachments/assets/76d5e06c-e6d4-4c97-b1aa-82dd1dfb491d" />


```
![Dashboard preview](docs/screenshot.png)
```

## Project Structure

```
week10/
├── app/
│   └── lecture10_exercise.py   # Main Streamlit application
├── data/
│   └── co2_emissions.csv       # Source dataset
└── README.md
```

> **Note:** The app expects `co2_emissions.csv` to live in a `data/` folder one level above the script (i.e., a sibling of `app/`). Keep this structure intact when cloning or moving the project.

## Data

| Column          | Description                              |
|-----------------|-------------------------------------------|
| `Country`       | Country name                              |
| `Region`        | Geographic region                         |
| `Year`          | Year of observation (2000–2022)           |
| `CO2_Mt`        | Total CO2 emissions, in megatonnes         |
| `CO2_per_capita`| CO2 emissions per capita                  |

Source: [Our World in Data — CO2 Emissions](https://ourworldindata.org/co2-emissions)

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
git clone (https://github.com/VallalaPurnachandar/dataviz-exercises-Purnachandar-Vallala.git)
cd dataviz-exercises-Purnachandar-Vallala.git/week10
pip install -r requirements.txt
```

If you don't have a `requirements.txt` yet, create one with:

```bash
pip install streamlit pandas plotly
pip freeze > requirements.txt
```

### Running the app

```bash
cd app
streamlit run lecture10_exercise.py
```

The app will open automatically in your browser at `http://localhost:8501`. If it doesn't, open that URL manually.

## Tech Stack

- [Streamlit](https://streamlit.io/) — app framework and UI widgets
- [Pandas](https://pandas.pydata.org/) — data loading and filtering
- [Plotly Express](https://plotly.com/python/plotly-express/) — interactive charts

## Design Notes

This project was built with two visualization design frameworks in mind:

- **Storytelling with Data (SWD):** white chart backgrounds, insight-driven titles that state the finding rather than just labeling the axes, and a grey-and-highlight color technique to draw attention to the top emitter.
- **Big Book of Dashboards (BBD):** always surfacing the record count so users know how much data underlies what they're seeing, and intentional (rather than default) color choices — categorical for multi-country comparisons, a single highlight color when calling out one country.

## License

This project is available under the MIT License. Feel free to adapt it for your own coursework or portfolio.

## Acknowledgments

- Dataset courtesy of [Our World in Data](https://ourworldindata.org/co2-emissions)
- Built as part of a data visualization course exercise (Lecture 10)

- 
App Deployment URL:https://dataviz-exercises-purnachandar-vallala-dd5w88tltwfyz4mxsdqbql.streamlit.app/
