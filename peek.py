import gzip

with gzip.open("data/2025-01-01-0.json.gz", "rt", encoding="utf-8") as f:
    for i in range(5):
        print(f.readline())