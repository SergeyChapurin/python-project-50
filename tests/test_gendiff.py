from gendiff import generate_diff


def test_generate_diff():
    file1_path = 'fixtures/file1.json'
    file2_path = 'fixtures/file2.json'


    expected_result = ('{\n' + '- follow: false\n' + '  host: hexlet.io\n'
                       + '- proxy: 123.234.53.22\n' + '- timeout: 50\n'
                       + '+ timeout: 20\n' + '+ verbose: true\n' + '}')

    result = generate_diff(file1_path, file2_path)

    assert result == expected_result


if __name__ == '__main__':
    test_generate_diff()

