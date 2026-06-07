import polars as pl

df = pl.scan_ndjson("data/2025-01-01-0.json.gz")

print(df.collect().head())