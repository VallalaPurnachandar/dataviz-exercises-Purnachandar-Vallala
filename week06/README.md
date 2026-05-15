# Week 6 Data Visualization Exercise

## Part-to-Whole: Hierarchical Visualization

This notebook is part of my Week 6 data visualization coursework. The exercise focuses on part-to-whole and hierarchical visualization using treemaps, sunburst charts, and a comparison bar chart.

The goal of this exercise is to show how energy production and spending totals can be broken down across meaningful categories while keeping the visualization clear, readable, and insight-driven.

## Dataset

The main dataset used in this exercise is:

```text
global_energy_mix.csv
```

It contains global energy mix information by country and source, including:

- Country
- Region
- Energy source
- Share percentage
- Energy generation in TWh

The notebook also uses Plotly's built-in `tips` dataset for the sunburst chart.

## Tools and Libraries

The analysis was completed using Python in a Jupyter Notebook.

Main libraries used:

- pandas
- numpy
- plotly.express

## Exercise Requirements

The notebook follows the Week 6 exercise rules:

1. Use Plotly Express first, then customize with `update_traces` and `update_layout`.
2. Colour must encode a meaningful category, not decoration.
3. Each chart title should describe a specific insight.
4. If a bar chart is clearer than a hierarchical chart, use the bar chart.

## Tasks Completed

### Task 1: Treemap of Fossil Fuel Dependency

A treemap was created using only fossil fuel sources:

- Coal
- Oil
- Natural Gas

The hierarchy is:

```text
Region -> Country -> Source
```

Colour is used to distinguish fossil fuel source type, while parent nodes are greyed out to keep attention on the energy sources.

Key finding:

Asia is the largest fossil-fuel region in the dataset, with approximately **35,284 TWh** from fossil sources. Saudi Arabia is the highest fossil-fuel country, with approximately **9,671 TWh**.

### Task 2: Sunburst of Tipping Behaviour

A sunburst chart was created using Plotly's built-in `tips` dataset. The chart shows how total bill amount is distributed across:

```text
Day -> Time -> Smoker status
```

The chart uses total bill value, not row counts. Colour identifies smoker status using a colour-vision-deficiency-safe blue and orange palette.

Key finding:

The largest spending concentration occurs during dinner, especially on weekend days. Saturday dinner is the strongest spending segment in the tips dataset.

### Task 3: Treemap vs Bar Chart for Low-Carbon Energy

Low-carbon energy was defined as:

- Nuclear
- Hydro

Two charts were created:

- A treemap showing part-to-whole contribution by country
- A horizontal bar chart sorted by total low-carbon TWh

Key finding:

France leads low-carbon energy generation in this dataset with approximately **7,593 TWh**, followed by Norway and Canada.

## Key Insights

The fossil fuel treemap shows that fossil energy use is concentrated heavily in Asia, with Saudi Arabia and China standing out at the country level.

The tips sunburst shows that spending is concentrated around dinner, especially on weekend days. This makes the sunburst useful for quickly seeing how total spending breaks down across day, meal time, and smoker status.

The low-carbon comparison shows that while a treemap is useful for part-to-whole structure, the horizontal bar chart is clearer for ranking countries. For comparing country totals, the bar chart communicates the result more directly.

## Files in This Repository

```text
week06/
  lecture06_exercise.ipynb

data/
  global_energy_mix.csv

README_week06.md
```

## How to Run the Notebook

1. Open the notebook:

```text
week06/lecture06_exercise.ipynb
```

2. Make sure the dataset is available at:

```text
data/global_energy_mix.csv
```

3. Run the notebook cells in order.

The notebook loads the dataset, creates the energy source category mapping, and generates the required hierarchical and comparison visualizations.

## Author

Student coursework submission for Week 6 Data Visualization.
