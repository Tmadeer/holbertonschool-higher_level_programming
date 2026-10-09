#!/usr/bin/env python3
"""Module for basic serialization of a dictionary to a JSON file."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to JSON and save it to filename."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load a JSON file and return the deserialized dictionary."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
