from gendiff.eng import generate_diff
from gendiff.tools import get_file_content
from gendiff.out_print import form_stylish, form_plain, form_json


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