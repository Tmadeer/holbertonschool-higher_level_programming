#!/usr/bin/env python3
"""Module that converts CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to data.json, return True on success."""
    try:
        with open(csv_filename, "r", newline="", encoding="utf-8") as f:
            data = list(csv.DictReader(f))
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
        return True
    except (OSError, csv.Error):
        return False
