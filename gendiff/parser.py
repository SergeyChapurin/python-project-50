import json
import os
import yaml
from gendiff.exceptions import UnknownFormatException


def read_file(file_path):
    _, extension = os.path.splitext(file_path)
    file_format = extension.lstrip(".")

    with open(file_path) as file:
        data = file.read()

    return data, file_format


def define_the_format(data, file_format):
    formats = {
        "yaml": yaml.safe_load,
        "yml": yaml.safe_load,
        "json": json.loads
    }

    if file_format not in formats:
        raise UnknownFormatException(f"Unknown format: {file_format}")

    return formats[file_format](data)


def get_data(file_path):
    data, file_format = read_file(file_path)
    return define_the_format(data, file_format)
