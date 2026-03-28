import sys, os, pandas as pd, requests

input_path = sys.argv[1] if len(sys.argv) > 1 else "data/nyc_arrests.csv"

if not os.path.exists(input_path):
    print("File not found. Downloading automatically...")
    url = "https://data.cityofnewyork.us/api/views/uip8-fykc/rows.csv?accessType=DOWNLOAD"
    os.makedirs(os.path.dirname(input_path), exist_ok=True)
    r = requests.get(url, stream=True)
    with open(input_path, "wb") as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)
    print("Download complete!")

df = pd.read_csv(input_path)
os.makedirs("data", exist_ok=True)
df.to_csv("data/data_raw.csv", index=False)
