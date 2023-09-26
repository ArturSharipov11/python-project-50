import pytest
from gendiff.parser import parse

@pytest.mark.parametrize('data, expected', [
    ('{"Hello": "World"}', {'Hello': 'World'}),
    ('Hello: World', {'Hello': 'World'}),
    ('Hello: World', {'Hello': 'World'})
])
def test_parse(data, expected):
    assert parse(data) == expected


def test_parse_invalid_format():
    with pytest.raises(ValueError):
        parse('Hello: World')
