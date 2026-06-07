import requests

files = [
    "2025-01-08-0.json.gz",
    "2025-01-15-0.json.gz",
    "2025-01-22-0.json.gz"
]

for filename in files:

    url = f"https://data.gharchive.org/{filename}"

    print(f"Downloading {filename}...")

    response = requests.get(url, stream=True)

    with open(f"data/{filename}", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"{filename} downloaded!")

print("All downloads complete!")