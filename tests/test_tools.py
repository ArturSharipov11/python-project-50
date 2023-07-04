from gendiff.tools import get_file_extension, load_file, get_file_content, map_value


def test_get_file_extension():
    assert get_file_extension('tests/files/file1.json') == '.json'


def test_load_file():
    assert load_file('tests/files/test') == 'Hello Hexlet!'


def test_get_file_content():
    assert get_file_content('tests/files/test.json') == {'Hello': 'World'}


def test_map_value():
    assert map_value({'key': 'value'}) == '[complex value]'
    assert map_value(True) == 'true'
    assert map_value('value') == "'value'"
    assert map_value(1) == 1