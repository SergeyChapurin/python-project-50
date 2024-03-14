import os
import pytest
from os.path import dirname, abspath
from gendiff import generate_diff


def get_abspath(file):
    return os.path.join(f'{dirname(abspath(__file__))}', 'fixtures', f'{file}')


test_data = [
    ('file1_nested.json', 'file2_nested.json', 'expected_res_stylish.txt', 'stylish'),
    ('file1_nested.yml', 'file2_nested.yml', 'expected_res_stylish.txt', 'stylish'),
    ('file1_nested.yml', 'file2_nested.yml', 'expected_res_plain.txt', 'plain'),
    ('file1_nested.json', 'file2_nested.json', 'expected_res_json.txt', 'json'),
]


@pytest.mark.parametrize("file1, file2, expected_res, format_name", test_data)
def test_generate_diff(file1, file2, expected_res, format_name):
    file1_path = get_abspath(file1)
    file2_path = get_abspath(file2)
    expected_res_path = get_abspath(expected_res)
    with open(expected_res_path, 'r') as file:
        result = file.read()
    assert generate_diff(file1_path, file2_path, format_name) == result
