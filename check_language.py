import gzip
import json

with gzip.open(
    "data/2025-01-01-0.json.gz",
    "rt",
    encoding="utf-8"
) as f:

    for line in f:
        obj = json.loads(line)

        if obj["type"] == "PullRequestEvent":

            try:
                lang = obj["payload"]["pull_request"]["base"]["repo"]["language"]

                print("Repository:",
                      obj["repo"]["name"])
                print("Language:",
                      lang)

                break

            except KeyError:
                pass