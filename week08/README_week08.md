# Week 8 Data Visualization Exercise

## Choropleth Maps

This notebook is part of my Week 8 data visualization coursework. The exercise focuses on choropleth maps using Plotly, with attention to geographic joins, colour scale choice, and insight-led map titles.

The main goal of this exercise is to create professional geographic visualizations that show how values differ across countries and regions.

## Datasets

The notebook uses two data sources:

```text
Plotly built-in Gapminder dataset
```

Used for the world life expectancy choropleth in Task 1.

```text
gapminder.csv
```

Used for the custom GeoJSON choropleth in Task 2. The file includes:

- Country
- Continent
- GDP per capita
- Life expectancy
- Population
- CO2 per capita

Task 2 also uses a free Natural Earth country GeoJSON file from geojson.xyz:

```text
https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_0_countries.geojson
```

## Tools and Libraries

The analysis was completed using Python in a Jupyter Notebook.

Main libraries used:

- pandas
- plotly.express
- plotly.graph_objects
- json
- urllib.request

## Exercise Requirements

The notebook follows the Week 8 exercise rules:

1. Use `px.choropleth` or `px.choropleth_map`.
2. Choose a colour scale that matches the data type.
3. Use an insight-driven title that states a geographic finding.
4. Correctly match the `featureidkey` to the GeoJSON properties.

## Tasks Completed

### Task 1: World Choropleth of Life Expectancy Deviation

A world choropleth was created using the built-in Gapminder dataset for 2007.

The chart shows each country's life expectancy relative to the global average. A diverging colour scale is used because the data contains values above and below zero.

Key finding:

African countries are furthest below the global average life expectancy in 2007, while many countries in Europe, Oceania, and parts of Asia are above the global average.

### Task 2: Custom GeoJSON Choropleth of CO2 per Capita

A custom choropleth was created using a Natural Earth country GeoJSON file and the provided local Gapminder-style dataset.

The chart maps CO2 emissions per capita by country. A sequential colour scale is used because CO2 per capita is a magnitude that increases from low to high.

Key finding:

Saudi Arabia has the highest CO2 per capita among the countries in the provided dataset, followed by Australia, Canada, and the USA.

## Key Insights

The life expectancy map shows a clear geographic divide. Countries in Africa are generally furthest below the 2007 global average, while Europe, Oceania, and several high-income countries are above average.

The CO2 per capita map shows that emissions intensity is not simply a population story. Some countries with smaller populations have very high per-person emissions, especially Saudi Arabia and Australia.

Together, the two maps show how choropleths can reveal geographic patterns clearly when the colour scale matches the data: diverging for above/below-average values and sequential for magnitude values.

## Files in This Repository

```text
week08/
  lecture08_exercise.ipynb

data/
  gapminder.csv

README_week08.md
```

## How to Run the Notebook

1. Open the notebook:

```text
week08/lecture08_exercise.ipynb
```

2. Make sure the local dataset is available at:

```text
data/gapminder.csv
```

3. Run the notebook cells in order.

Task 2 downloads a free GeoJSON file from geojson.xyz, so an internet connection is required for that cell.

## Author

Student coursework submission for Week 8 Data Visualization.
