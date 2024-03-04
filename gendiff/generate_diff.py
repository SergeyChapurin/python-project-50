from gendiff.read_files import read_file, load_data
from gendiff.build_diff import build_diff
from gendiff.formatters.format_name import get_format_name


def generate_diff(file1_path, file2_path, format_name):
    read_data1, file1_format = read_file(file1_path)
    read_data2, file2_format = read_file(file2_path)

    data1 = load_data(read_data1, file1_format)
    data2 = load_data(read_data2, file2_format)

    diff = build_diff(data1, data2)
    return get_format_name(diff, format_name)
