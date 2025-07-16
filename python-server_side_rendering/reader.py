import json
import csv

def read_products_from_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def read_products_from_csv(filename):
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
            for item in data:
                item["id"] = int(item["id"])
                item["price"] = float(item["price"])
            return data
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []
