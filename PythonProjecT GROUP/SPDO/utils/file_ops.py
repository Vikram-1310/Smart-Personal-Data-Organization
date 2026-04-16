import json
import csv

def write_json(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def read_json(filename="data.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except:
        return []

def write_csv(data, filename="data.csv"):
    if len(data) == 0:
        return

    keys = data[0].keys()
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)