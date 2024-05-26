---
created: 2024-05-06 20:10:45-07:00
title: Data Visualization
updated: 2024-05-06 20:18:45-07:00
---

## Summary

Transformation of complex data into a visual form — possibly interactive — to more easily comprehend trends, outliers, and significant patterns in large data sets.

## Jots

also: *InfoVis*, *DataVis*, or even just *viz*

Key attributes to ponder

* scalability to large number of data
* interactivity for multiple views

### Why?

* Involve lizard brain in data analysis process. Lizard brain quickly notice patterns and changes in display of data to support ape-brain understanding and decision-making.
* Interactive data visualization can also engage as a form of play – I know we are describing *very important things* with that data, but "what if we change that value or reassign this axis" is also make fun colors move go pretty sparkly oh no that bit look wrong please fix this, ape-brain.

### When?

* when there's a common underlying structure
* when users don't know the details of a collection
* when users don't understand how the collection is organized (show vs tell for learning)
* when info is easier to recognize than to describe

### Subfields of Data Visualization

scientific visualization
: model real-world phenomena

information visualization
: present abstract concepts for decision making and analysis

visual analytics
: combining interactive visualization with data analysis and transformation to enable high-level activities like sense-making and decision-making.

## Chart Types

* Bar Chart
  * for grouping by category or illustrating discrete variables
* Histogram
  * groups data into bins to show distribution over a continuous interval or time period
  * helps identify trends, outliers, patterns, and anomalies
* Line Chart
  * lines connecting Cartesian points
* Stacked Chart
  * compare different categories and total sizes at the same time
* Scatter Plot
  * uses Cartesian coordinates to show values over two variables
* Heatmap
  * Represent matrix values in a heatmap as colors, representing degree or strength of an occurrence with differing shades or intensities.
  * useful for pattern recognition and outlier detection
* Funnel Chart
  * Displays values in progressively diminishing stages, to better understand those stages and how they contribute to a system's output
* Pie Chart
  * a circle divided into slices to visualize simple categorization and grouping of variables
  * best for a small number of categories with obvious proportions.

## Data Visualization Tools

* [Pandas](Pandas.md) and other *DataFrame* toolkits make frequent appearances with data visualization tools. Many of the listed data visualization tools are [Python](Python.md) because it's a popular choice but also because that's mostly what I know. I hope to fill in some gaps later.
* Bokeh
  * Python library for Web-based data visualization
  * [Bokeh documentation](https://docs.bokeh.org/en/latest/)
* D3.js
  * Popular data visualization library for [JavaScript](JavaScript.md)
  * [D3 by Observable | The JavaScript library for bespoke data visualization](https://d3js.org/)
* ggplot2
  * A data visualization tool for the R programming language with an API based on [The Grammar of Graphics](https://www.amazon.com/Grammar-Graphics-Statistics-Computing/dp/0387245448)
  * [plotnine - A Grammar of Graphics for Python](https://plotnine.org) #Python
* Holoviz
  * A whole suite of high-level tools and libraries for more powerful data visualization applications. Many of these tools show off their best side from inside a Jupyter notebook.
    * **Panel**
      * for creating and maintaining DataViz tools, dashboards, and applications in Python
      * [Overview — Panel](https://panel.holoviz.org/)
    * **hvPlot**
      * API for data visualization and exploration
      * [hvPlot](https://hvplot.holoviz.org/)
    * **HoloViews**
      * pretty handy for live exploration of data
      * [HoloViews](https://holoviews.org/)
    * **GeoViews**
      * visualization and exploration of geographical, meteorological, and oceanographic data
      * [GeoViews](https://geoviews.org/)
    * **Datashader**
      * Pipeline for visualization of large datasets
      * [Datashader](https://datashader.org/)
    * **Lumen**
      * declarative framework for data dashboards
      * [Welcome to Lumen!](https://lumen.holoviz.org/)
    * **Param**
      * Parameter declaration in Python
      * Loads of overlap with *Pydantic* and *attrs*, but it's a tight enough API to still be worthwhile as a concise means of expressing type information and validation requirements.
      * [Welcome to Param!](https://param.holoviz.org/)
    * ## **Colorcet**
      
      ````
      > a collection of perceptually accurate 256-color colormaps for use with Python plotting progams  
      ````
      
      * [Collection of perceptually accurate colormaps](https://colorcet.holoviz.org/)
  * [High-level tools to simplify visualization in Python — HoloViz](https://holoviz.org/)
* matplotlib
  * Possibly the most widely known data visualization library for Python?
  * [Matplotlib — Visualization with Python](https://matplotlib.org/)
  * seaborn
    * High-level interface to matplotlib
    * [seaborn: statistical data visualization — seaborn 0.13.2 documentation](https://seaborn.pydata.org/)
* Plotly
  * Company producing commercial and open source tools for data visualization. I'll focus on the open source stuff until I need to concern myself with their commercial offerings.
  * [Plotly: Low-Code Data App Development](https://plotly.com/)
  * Plotly Graphing Libraries
    * API for interactive data visualization available in several languages
    * [Plotly Open Source Graphing Libraries](https://plotly.com/graphing-libraries/)
  * Dash
    * Plotly's low-code framework for data applications
    * https://dash.plotly.com/
* Power BI
  * data visualization tool from *Microsoft*
  * [Power BI - Data Visualization | Microsoft Power Platform](https://www.microsoft.com/power-platform/products/power-bi)
* Tableau
  * No-code tool for transforming, understanding, and visualizing raw data
  * [Business Intelligence and Analytics Software | Tableau](https://www.tableau.com/)
* Vega-Altair
  * Python library for data visualization using the Vega-Lite grammar. I enjoyed using this one because of its consistent language which I could understand even without a strong backing in data visualization.
  * [Vega-Altair: Declarative Visualization in Python — Vega-Altair 5.3.0 documentation](https://altair-viz.github.io/)
  * [A High-Level Grammar of Interactive Graphics | Vega-Lite](https://vega.github.io/vega-lite/)

## Related

* [Data Analysis](Data%20Analysis.md)
* *Data Science*
* [Key Concepts of Data Visualization](https://maelfabien.github.io/machinelearning/Dataviz/#) #Media/BlogPost