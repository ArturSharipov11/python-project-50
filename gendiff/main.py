from gendiff.eng import generate_diff
from gendiff.assistants.about_file import get_file_content
from gendiff.formats.stylish import form_stylish
from gendiff.formats.plain import form_plain
from gendiff.formats.json import form_json


def gen_diff(first_file, second_file, output_type='stylish'):
    dict1 = get_file_content(first_file)
    dict2 = get_file_content(second_file)
    diff_tree = generate_diff(dict1, dict2)
    if output_type == 'plain':
        return form_plain(diff_tree)[:-1]
    elif output_type == 'json':
        return form_json(diff_tree)
    else:
        return form_stylish(diff_tree)
