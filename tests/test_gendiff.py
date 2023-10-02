from gendiff.main import generate_diff
import pytest


@pytest.mark.parametrize("file1, file2, correct_outputs, format_output", [
    (
        './tests/fixtures/file1.yml',
        './tests/fixtures/file2.yml',
        './tests/fixtures/right_sim.txt',
        'stylish'
    ),
    (
        './tests/fixtures/file1.json',
        './tests/fixtures/file2.json',
        './tests/fixtures/right_sim.txt',
        'stylish'
    ),
    (
        './tests/fixtures/file1_tree.json',
        './tests/fixtures/file2_tree.json',
        './tests/fixtures/right_stylish.txt',
        'stylish'
    ),
    (
        './tests/fixtures/file1_tree.yml',
        './tests/fixtures/file2_tree.yml',
        './tests/fixtures/right_stylish.txt',
        'stylish'
    ),
    (
        './tests/fixtures/file1_tree.json',
        './tests/fixtures/file2_tree.json',
        './tests/fixtures/right_plain.txt',
        'plain'
    ),
    (
        './tests/fixtures/file1_tree.yml',
        './tests/fixtures/file2_tree.yml',
        './tests/fixtures/right_plain.txt',
        'plain'
    ),
    (
        './tests/fixtures/file1_tree.json',
        './tests/fixtures/file2_tree.json',
        './tests/fixtures/right_json.txt',
        'json'
    ),
    (
        './tests/fixtures/file1_tree.yml',
        './tests/fixtures/file2_tree.yml',
        './tests/fixtures/right_json.txt',
        'json'
    ),
])
def test_generate_diff(file1, file2, correct_outputs, format_output):
    with open(correct_outputs) as f:
        expected = f.read()
    eval_result = generate_diff(file1, file2, format_output)
    assert eval_result == expected.rstrip('\n')
    