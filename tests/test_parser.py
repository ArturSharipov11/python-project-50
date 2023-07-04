import pytest

from gendiff.parser import parse


def test_parse():
    assert parse('{"Hello": "World"}', '.json') == {'Hello': 'World'}
    assert parse('Hello: World', '.yaml') == {'Hello': 'World'}
    assert parse('Hello: World', '.yml') == {'Hello': 'World'}
    with pytest.raises(ValueError):
        parse('Hello: World', '.txt')