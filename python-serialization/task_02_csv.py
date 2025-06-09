#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        data = []
        with open(csv_filename, 'r', encoding='utf-8') as task_02_cvs:
            cvs_reader = csv.DictReader(task_02_cvs)
            for row in cvs_reader:
                data.append(row)

        json_data = json.dump(data, indent=4)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)

        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        return False
