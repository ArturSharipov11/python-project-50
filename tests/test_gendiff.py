from gendiff.main import generate_diff
from itertools import cycle, repeat
import pytest

first_version_files = (
    './tests/fixtures/file1_tree.json',
    './tests/fixtures/file1_tree.yml',
)

second_version_files = (
    './tests/fixtures/file2_tree.json',
    './tests/fixtures/file2_tree.yml',
)

pass_correct_outputs = (
    './tests/fixtures/right_stylish.txt',
    './tests/fixtures/right_plain.txt',
    './tests/fixtures/right_json.txt'
)

correct_output_stylish = './tests/fixtures/right_stylish.txt'
correct_output_plain = './tests/fixtures/right_plain.txt'
correct_output_json = './tests/fixtures/right_json.txt'


stylish_format_output = 'stylish'
plain_format_output = 'plain'
json_format_output = 'json'


@pytest.mark.parametrize(
    'file1, file2, correct_outputs, format_output',
    [
        (file1, file2, correct_outputs, format_output)
        for (file1, file2, correct_outputs, format_output) in zip(
            cycle(first_version_files),
            cycle(second_version_files),
            [
                *repeat(correct_output_stylish, 2),
                *repeat(correct_output_plain, 2),
                *repeat(correct_output_json, 2),
            ],
            [
                *repeat(stylish_format_output, 2),
                *repeat(plain_format_output, 2),
                *repeat(json_format_output, 2),
            ]
        )

    ]
)
def test_generate_diff(file1, file2, correct_outputs, format_output):
    with open(correct_outputs) as f:
        expected = f.read()
    eval_result = generate_diff(file1, file2, format_output)
    assert eval_result == expected.rstrip('\n')
