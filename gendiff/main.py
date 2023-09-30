from gendiff.eng import get_comparison_results
from gendiff.load import loading
from gendiff.formats.stylish import stylish_view
from gendiff.formats.plain import flatten
from gendiff.formats.json import form_json


def generate_diff(first_file, second_file, format='stylish'):
    dict1 = loading(first_file)
    dict2 = loading(second_file)
    diff = get_comparison_results(dict1, dict2)
    if format == 'plain':
        return flatten(diff)
    elif format == 'json':
        return form_json(diff)
    return stylish_view(diff)
