from gendiff.read_files import read_file, load_data


def generate_diff(file1_path, file2_path):
    read_data1, file1_format = read_file(file1_path)
    read_data2, file2_format = read_file(file2_path)
    data1 = load_data(read_data1, file1_format)
    data2 = load_data(read_data2, file2_format)
    result_lines = []

    for key in sorted(set(data1.keys()) | set(data2.keys())):
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in data1 and key in data2:
            if value1 == value2:
                result_lines.append(f'    {key}: {format_value(value1)}')
            else:
                result_lines.append(f'  - {key}: {format_value(value1)}')
                result_lines.append(f'  + {key}: {format_value(value2)}')

        elif key in data1:
            result_lines.append(f'  - {key}: {format_value(value1)}')

        elif key in data2:
            result_lines.append(f'  + {key}: {format_value(value2)}')

    return '{\n' + '\n'.join(result_lines) + '\n}'


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value
