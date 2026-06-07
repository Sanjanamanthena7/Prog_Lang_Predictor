import gzip
import json

records = []

with gzip.open("data/2025-01-01-0.json.gz", "rt", encoding="utf-8") as f:
    for i, line in enumerate(f):
        records.append(json.loads(line))

        if i >= 9:
            break

print("Records:", len(records))

print("\nKeys:")
print(records[0].keys())

print("\nFirst Record:")
print(records[0])