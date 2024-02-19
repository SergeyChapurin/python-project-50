from gendiff import generate_diff


def test_generate_diff():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'

    file_path3 = 'tests/fixtures/file1.yaml'
    file_path4 = 'tests/fixtures/file2.yaml'
    file_path5 = 'tests/fixtures/expected_result.txt'

    with open(file_path5, 'r') as file:
        expected_result = file.read()




    result_json = generate_diff(file_path1, file_path2)
    result_yaml = generate_diff(file_path3, file_path4)

    assert result_json == expected_result
    assert result_yaml == expected_result
    print(result_json)
    print(result_yaml)
    print(expected_result)




if __name__ == '__main__':
    test_generate_diff()

