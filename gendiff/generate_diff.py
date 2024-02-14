#!/usr/bin/env python3


import json


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    result_lines = []

    for key in sorted(set(data1.keys()) | set(data2.keys())):
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in data1 and key in data2:
            if value1 == value2:
                result_lines.append(f'  {key}: {format_value(value1)}')
            else:
                result_lines.append(f'- {key}: {format_value(value1)}')
                result_lines.append(f'+ {key}: {format_value(value2)}')
        elif key in data1:
            result_lines.append(f'- {key}: {format_value(value1)}')
        elif key in data2:
            result_lines.append(f'+ {key}: {format_value(value2)}')

    return '{\n' + '\n'.join(result_lines) + '\n}'
