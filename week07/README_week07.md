# Week 7 Data Visualization Exercise

## Heatmap & Waterfall: Netflix Catalogue

This notebook is part of my Week 7 data visualization coursework. The exercise focuses on heatmaps and waterfall charts using a Netflix catalogue dataset.

The goal of this exercise is to show how different visualization types can communicate different analytical stories: heatmaps for comparing category combinations and waterfall charts for showing cumulative growth over time.

## Dataset

The dataset used in this exercise is:

```text
netflix_catalogue.csv
```

It contains Netflix catalogue information, including:

- Content type
- Release year
- Year added to Netflix
- Genre
- Country
- Content rating
- Duration

## Tools and Libraries

The analysis was completed using Python in a Jupyter Notebook.

Main libraries used:

- pandas
- plotly.express
- plotly.graph_objects

## Exercise Requirements

The notebook follows the Week 7 exercise rules:

1. Heatmap colour scale must match the data type.
2. Waterfall chart must use green for additions, red for subtractions, and blue for totals.
3. Chart titles should explain the main insight or story.
4. At least one heatmap cell or waterfall bar must be directly annotated.

## Tasks Completed

### Task 1: Heatmap of Content Rating by Release Decade

A heatmap was created to show the number of Netflix titles by content rating and release decade.

The analysis focuses on the five most common ratings:

- TV-14
- TV-MA
- PG-13
- R
- PG

The heatmap uses a sequential blue colour scale because the data represents counts. Cell values are shown directly inside the heatmap.

Key finding:

The largest concentration is **TV-MA titles from the 2010s**, with **359 titles**. TV-MA also has a very strong presence in the 2000s, showing that mature-audience content is a major part of the catalogue.

### Task 2: Waterfall Chart of Movie Additions

A waterfall chart was created to show how Netflix's movie library grew year by year from **2015 to 2022**.

The chart counts Movie titles added each year and ends with a cumulative total bar. Green bars represent yearly additions, and the blue bar represents the final cumulative total.

Key finding:

Netflix added **659 movies** between 2015 and 2022. The biggest single-year additions occurred in **2016** and **2019**, with **93 movies** added in each year.

## Key Insights

The heatmap shows that adult and teen-oriented content dominates the Netflix catalogue, especially TV-MA and TV-14 titles from the 2000s and 2010s.

The waterfall chart shows steady movie catalogue growth from 2015 to 2022 rather than one single dramatic spike. The largest annual additions happened in 2016 and 2019, but the year-to-year pattern remains relatively stable.

## Files in This Repository

```text
week07/
  lecture07_exercise.ipynb

data/
  netflix_catalogue.csv

README_week07.md
```

## How to Run the Notebook

1. Open the notebook:

```text
week07/lecture07_exercise.ipynb
```

2. Make sure the dataset is available at:

```text
data/netflix_catalogue.csv
```

3. Run the notebook cells in order.

The notebook loads the Netflix catalogue dataset, prepares the required grouping columns, and generates the heatmap and waterfall visualizations.

## Author

Student coursework submission for Week 7 Data Visualization.
