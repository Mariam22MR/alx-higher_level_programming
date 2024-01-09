#!/usr/bin/python3
"""Defination of JSON file-reading function."""
import json


def load_from_json_file(filename):
    """create python object from JSON file."""
    with open(filename) as f:
        return json.load(f)
