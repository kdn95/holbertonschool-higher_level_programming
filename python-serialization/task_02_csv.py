#!/usr/bin/python3
"""Converting CSV to JSON format"""
import csv
import json


def convert_csv_to_json(CSVFile):
    """CSV to json"""
    try:
        my_dict = []
        with open(CSVFile,"r", encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                my_dict.append(row)

        with open('data.json', "w", encoding='utf-8') as json_file:
            json.dump(my_dict, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
