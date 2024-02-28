from gendiff import generate_diff


def test_generate_diff():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'

    file_path3 = 'tests/fixtures/file1.yaml'
    file_path4 = 'tests/fixtures/file2.yaml'

    file_path5 = 'tests/fixtures/expected_result.txt'

    file_path6 = 'tests/fixtures/file1_nested.json'
    file_path7 = 'tests/fixtures/file2_nested.json'

    file_path8 = 'tests/fixtures/file1_nested.yml'
    file_path9 = 'tests/fixtures/file2_nested.yml'

    file_path10 = 'tests/fixtures/expected_res_nested.txt'

    with open(file_path5, 'r') as file:
        expected_result = file.read()

    with open(file_path10, 'r') as file:
        expected_res_nested = file.read()

    result_json = generate_diff(file_path1, file_path2, format='stylish')
    result_yaml = generate_diff(file_path3, file_path4, format='stylish')
    result_json_nested = generate_diff(file_path6, file_path7, format='stylish')
    result_yaml_nested = generate_diff(file_path8, file_path9, format='stylish')

    assert result_json == expected_result
    assert result_yaml == expected_result
    assert result_json_nested == expected_res_nested
    assert result_yaml_nested == expected_res_nested


if __name__ == '__main__':
    test_generate_diff()

