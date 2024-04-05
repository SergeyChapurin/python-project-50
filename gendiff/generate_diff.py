from gendiff.parser import get_data
from gendiff.build_diff import build_diff
from gendiff.formatters import get_format_name


def generate_diff(file1_path, file2_path, format_name='stylish'):
    data1 = get_data(file1_path)
    data2 = get_data(file2_path)

    diff = build_diff(data1, data2)
    return get_format_name(diff, format_name)
