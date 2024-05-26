---
created: 2024-05-06 15:31:41-07:00
title: Polars
updated: 2024-05-06 15:33:35-07:00
---

## Summary

Fast *DataFrame* framework for [Data Analysis](Data%20Analysis.md)

## Jots

````python
import polars as pl
````

### Read a [CSV](CSV.md) file with Polars #process

`read_csv` to immediately read, like in [Pandas](Pandas.md)

````python
df = pl.read_csv(CSV_PATH)
````

`scan_csv` for lazy loading, which allows optimizations for large / fancy data files

````python
query = pl.scan_csv(CSV_PATH)
# do your filters and transforms to the query
# then when you're ready to interact with it:
df = query.collect()
````

### Polars Ruby

A [Ruby](Ruby.md) interface to Polars

````sh
gem install polars-df
````

[GitHub - ankane/polars-ruby: Blazingly fast DataFrames for Ruby](https://github.com/ankane/polars-ruby)

## Related

* [Polars — DataFrames for the new era](https://pola.rs)