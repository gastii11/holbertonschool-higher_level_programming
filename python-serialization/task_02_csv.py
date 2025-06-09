#!/usr/bin/env python3
import csv
import json
import os


def convert_csv_to_json(csv_filename):
    try:
        if not os.path.exists(csv_filename):
            with open('data.json', 'w') as json_file:
                json.dump([], json_file)
            return False

        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception as e:
        with open('data.json', 'w') as json_file:
            json.dump([], json_file)
        return False
