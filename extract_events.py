import gzip
import json
import polars as pl

records = []

with gzip.open(
    "data/2025-01-01-0.json.gz",
    "rt",
    encoding="utf-8"
) as f:

    for line in f:
        event = json.loads(line)

        records.append({
            "event_type": event["type"],
            "repo_name": event["repo"]["name"],
            "created_at": event["created_at"]
        })

        # only first 10000 rows for testing
        if len(records) >= 10000:
            break

df = pl.DataFrame(records)

print(
    df.select("repo_name")
      .unique()
      .head(20)
)

print(
    "Unique repos:",
    df.select("repo_name").n_unique()
)