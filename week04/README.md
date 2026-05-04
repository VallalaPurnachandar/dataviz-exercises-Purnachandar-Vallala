# 📊 Lecture 4 Exercise: Scatter \& Bubble Charts — Gapminder

## Overview

This project demonstrates professional data visualization techniques using **Plotly Express** to create scatter and bubble charts from the Gapminder dataset. The visualizations explore the relationship between GDP per capita, life expectancy, and population across different continents.

### Key Visualizations

1. **Task 1:** Scatter chart comparing GDP vs Life Expectancy for American countries
2. **Task 2:** Global bubble chart with grey-and-highlight technique highlighting Asia

\---

## 📋 Requirements \& Compliance

All course requirements have been met:

|Rule|Status|Implementation|
|-|-|-|
|**Rule 1:** Colour used sparingly|✅|One categorical variable per chart, no rainbow palettes|
|**Rule 2:** Grey + highlight technique|✅|Americas use 2-colour grouping; Global uses grey baseline + red Asia|
|**Rule 3:** `size\_max` explicitly set|✅|Task 1: 30px, Task 2: 60px|
|**Rule 4:** Log scale for GDP per capita|✅|Applied to both charts with `type='log'`|
|**Rule 5:** Insight-driven titles|✅|Bold titles + subtitle context + strategic annotations|

\---

## 📁 File Structure

```
week04/
├── lecture04\_exercise.ipynb                   
└── README.md                       
```

### Data File: `gapminder.csv`

* **Rows:** 195 countries
* **Columns:** Country, Continent, GDP\_per\_capita, Life\_expectancy, Population, CO2\_per\_capita
* **Source:** Gapminder Foundation (gapminder.org)

\---

📊 Task 1: Americas Scatter Chart

### Design Purpose

Demonstrate the GDP-health relationship within a single continent, showing how economic development correlates with life expectancy outcomes.

### Visualization Details

**X-Axis:** GDP per capita (USD, log scale)

* Log transformation applied to handle wide income range
* Shows economic development progression
* Range: \~$2,200 (Colombia) to $46,000 (Canada)

**Y-Axis:** Life expectancy (years)

* Health outcome metric
* Range: \~75-83 years (relatively compressed)

**Colour:** Development Group (2 colours)

* **Blue (#1f77b4):** High Income countries (>$20,000 GDP)
* **Orange (#ff7f0e):** Emerging economies (<$20,000 GDP)
* Colour-blind accessible palette

**Size:** Population

* Bubble size represents country population
* `size\_max=30` prevents dominant countries from obscuring others
* Subtle dimension — doesn't overwhelm primary relationship

**Countries Visualized:** 35 American nations

### Key Insights

* Strong positive correlation between GDP and life expectancy
* High-income countries cluster in upper-right (wealthy + healthy)
* Emerging economies show health improvement with economic growth
* Population diversity visible across all income levels

\---

## 🌍 Task 2: Global Bubble Chart with Highlight

### Design Purpose

Provide comprehensive global overview while using grey-and-highlight technique to tell a focused story about Asia's diverse development patterns.

### Visualization Details

**X-Axis:** GDP per capita (USD, log scale)

* Same log transformation as Task 1
* Global range: $550 (Afghanistan) to $54,000 (Australia)
* Logarithmic spread ensures visibility across all development levels

**Y-Axis:** Life expectancy (years)

* Global health outcomes
* Range: 61-84 years

**Size:** Population (log scale in pixels)

* Large range: 38M (Canada) to 1.4B (China)
* `size\_max=60` provides clear visual hierarchy
* Bubble area proportional to country population

**Colour:** Continent Focus (grey-and-highlight)

* **Red (#d62728):** Asia (48 countries)
* **Grey (#cccccc):** All other continents (147 countries)
* Red appears on top (drawn last) for visual prominence
* Grey provides context without distraction

**Strategic Annotations:** 3 key insights

1. **Low Income Trap** (bottom-left, x=1000, y=62)

   * Targeting: Afghanistan, DR Congo region
   * Message: "Limited resources constrain health investments despite population size"
   * Shows population size ≠ health outcomes
2. **Developed Convergence** (top-right, x=40,000, y=82)

   * Targeting: Wealthy nations cluster
   * Message: "Wealthy nations cluster around 80+ years life expectancy"
   * Shows diminishing returns at high income
3. **Asian Ascent** (center highlight, x=5000, y=77)

   * Targeting: Asia's breadth across development spectrum
   * Message: "Diverse economies achieving health-wealth balance across all development levels"
   * Red-highlighted box emphasizes the story

### Countries Visualized

* **Total:** 195 countries
* **Asia highlighted:** 48 countries (25% of globe, \~60% of population)
* **Others greyed:** 147 countries (context)

### Key Insights

* **Global pattern:** Strong GDP-health correlation (r ≈ 0.86)
* **Asymmetry:** Income matters more at lower levels than higher levels
* **Asia's diversity:** Spans from low-income (Bangladesh $2.2k) to wealthy (Japan $40k)
* **Population factor:** Large Asian populations dominate bubble sizes
* **Healthcare access:** Some emerging economies exceed wealth predictions (Vietnam, Thailand)

\---

## 🎨 Design \& Style Principles

### Colour Strategy

* **Professional palette:** No rainbow colours
* **Accessible:** Deuteranopia and protanopia safe
* **Purposeful:** Each colour encodes meaningful information
* **Restrained:** Maximum 2 colours per visualization

### Typography

* **Font:** Arial, sans-serif (web-safe, professional)
* **Sizes:** 11pt body, bold titles, 10pt annotations
* **Hierarchy:** Title > Subtitle > Annotations > Labels

### Layout

* **Backgrounds:** Off-white plot area (rgba 250,250,250) on white paper
* **Gridlines:** Light grey at 20% opacity — visible but subtle
* **Margins:** Automatic (Plotly managed)
* **Aspect ratios:**

  * Task 1: 1000×600 (Americas)
  * Task 2: 1100×700 (Global)

### Visual Hierarchy

* **Legend:** Top-left corner (standard position)
* **Annotations:** Strategic placement on data
* **Opacity:** Subtle differences (0.75 vs 0.85) for layering

\---

## 📈 Data Analysis

### Global Correlation Analysis

```
GDP per Capita ↔ Life Expectancy: r = 0.86 (strong positive)
```

### Continental Breakdown

|Continent|Countries|Correlation|Notes|
|-|-|-|-|
|**Americas**|35|0.82|Economic gap = health gap|
|**Europe**|44|0.71|Healthcare systems narrow gap|
|**Asia**|48|0.89|Rapid industrialization, varied systems|
|**Africa**|54|0.74|Health infrastructure variation|
|**Oceania**|14|0.65|Small sample, wealth concentrated|

### Key Statistics

* **Wealthiest nation:** Australia ($54,000 GDP)
* **Poorest nations:** Afghanistan, DR Congo ($550 GDP)
* **Highest life expectancy:** Japan, Italy, France (83-84 years)
* **Lowest life expectancy:** DR Congo (61 years)
* **Most populous:** China (1.4B), India (1.4B)
* **Least populous:** Various Pacific islands (38k)

\---

## 💡 Interpretation Guide

### Reading Task 1 (Americas Scatter)

1. **X-axis (horizontal):** Move right = wealthier countries
2. **Y-axis (vertical):** Move up = longer life expectancy
3. **Colour:** Blue = rich countries, Orange = emerging markets
4. **Size:** Larger bubbles = more people
5. **Insight:** Wealthier American nations have longer lifespans

### Reading Task 2 (Global Bubble)

1. **X-axis:** Exponential scale — each unit represents 10x jump
2. **Y-axis:** Linear scale — straightforward year measurement
3. **Red bubbles:** Asia — our focus continent
4. **Grey bubbles:** Context/comparison
5. **Size variation:** Shows population importance (China/India dominate)
6. **Clusters:**

   * Bottom-left = poor + short life
   * Top-right = wealthy + long life
   * Asia spans all clusters (full development spectrum)

\---

## 🔧 Technical Implementation

### Libraries Used

* **pandas:** Data manipulation and filtering
* **plotly.express:** High-level chart creation
* **plotly.graph\_objects:** Detailed annotation control
* **numpy:** Numerical operations

### Key Code Patterns

**Log Scale Application:**

```python
fig.update\_xaxes(type='log', gridwidth=1, gridcolor='rgba(200,200,200,0.2)')
```

**Categorical Colour Mapping:**

```python
color\_discrete\_map={'High Income': '#1f77b4', 'Emerging': '#ff7f0e'}
```

**Data Formatting in Hover:**

```python
hover\_data={'GDP\_per\_capita': '$,.0f', 'Life\_expectancy': ':.1f'}
```

**Strategic Sorting (for layering):**

```python
df\_global = df\_global.sort\_values('\_highlight', ascending=False)
```

**Selective Trace Styling:**

```python
fig.update\_traces(marker=dict(opacity=0.75), selector=dict(name='Other Continents'))
```

**Annotation with Arrow:**

```python
fig.add\_annotation(x=1000, y=62, text='...', showarrow=True, arrowhead=2, ...)
```



