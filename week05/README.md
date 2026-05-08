# Week 5 Data Visualization Exercise

## Distribution Charts: Airbnb London

This notebook is part of my Week 5 data visualization coursework. The exercise focuses on creating effective distribution charts using Airbnb listing data from London.

The main goal of this task is to explore how Airbnb prices and listing activity vary across room types and boroughs, while applying good visualization principles such as outlier handling, meaningful colour use, reference lines, and insight-driven chart titles.

## Dataset

The dataset used in this exercise is:

```text
airbnb_london.csv
```

It contains Airbnb listing information for London, including:

- Neighbourhood / borough
- Room type
- Nightly price
- Minimum nights
- Number of reviews
- Availability across the year
- Reviews per month

## Tools and Libraries

The analysis was completed using Python in a Jupyter Notebook.

Main libraries used:

- pandas
- numpy
- plotly.express
- plotly.graph_objects

## Exercise Requirements

The notebook follows the Week 5 exercise rules:

1. Price outliers are capped at the 95th percentile.
2. Each chart includes a mean or median reference line.
3. Each chart has an insight-driven title.
4. Colour is used meaningfully, not only for decoration.

## Tasks Completed

### Task 1: Histogram of Price by Room Type

A histogram was created to compare nightly price distributions for:

- Entire home/apartment
- Private room

Shared rooms were excluded because they had fewer observations.

The chart uses overlapping histograms with transparent bars so both distributions can be compared clearly. Median price reference lines were added for each room type.

Key finding:

Entire homes/apartments have a much higher median nightly price than private rooms. After capping price outliers at the 95th percentile, the median price for an entire home/apartment is approximately **£163**, compared with approximately **£79** for a private room.

### Task 2: Box Plot of Listing Activity by Borough

A horizontal box plot was created to compare listing activity across London boroughs.

Reviews per month were used as a proxy for listing activity. Listings with zero reviews were removed because they may represent new or inactive listings.

The boroughs were sorted by median reviews per month, and the two most active boroughs were highlighted.

Key finding:

**Tower Hamlets** and **Hackney** have the highest median listing activity. Tower Hamlets has a median of approximately **1.76 reviews per month**, while Hackney has approximately **1.66 reviews per month**.

## Key Insights

The analysis shows that Airbnb prices in London are strongly influenced by room type. Entire homes/apartments are generally much more expensive and have a wider price spread, while private rooms are more concentrated at lower prices.

The activity analysis shows that Airbnb demand is not evenly distributed across boroughs. Some boroughs, especially Tower Hamlets and Hackney, appear to have more active listings based on review frequency.

## Files in This Repository

```text
week05/
  lecture05_exercise.ipynb
  README.md
```

## How to Run the Notebook

1. Open the notebook:

```text
week05/lecture05_exercise.ipynb
```

2. Make sure the dataset is available at:

```text
data/airbnb_london.csv
```

3. Run the notebook cells in order.

The notebook will load the dataset, cap price outliers at the 95th percentile, and generate the required visualizations.

## Author
VALLALA PURNACHANDAR
Student coursework submission for Week 5 Data Visualization.
