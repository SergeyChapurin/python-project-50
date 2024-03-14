import json
import os
import yaml


def read_file(file_path):
    _, extension = os.path.splitext(file_path)
    file_format = extension.lstrip(".")

    with open(file_path) as file:
        data = file.read()

    return data, file_format


def load_data(data, file_format):
    formats = {
        "yaml": yaml.safe_load,
        "yml": yaml.safe_load,
        "json": json.loads
    }

    if file_format not in formats:
        raise UnsupportedFormatException(f"Unsupported format: {file_format}")

    return formats[file_format](data)
