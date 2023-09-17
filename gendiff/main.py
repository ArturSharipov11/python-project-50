from gendiff.eng import gen_diff
from gendiff.assistants.about_file import get_file_content
from gendiff.formats.stylish import form_stylish
from gendiff.formats.plain import form_plain
from gendiff.formats.json import form_json


def generate_diff(first_file, second_file, output_type='stylish'):
    dict1 = get_file_content(first_file)
    dict2 = get_file_content(second_file)
    diff_tree = gen_diff(dict1, dict2)
    
    format_functions = {
        'plain': lambda tree: form_plain(tree)[:-1],
        'json': lambda tree: form_json(tree),
        'stylish': lambda tree: form_stylish(tree),
    }
    
    return format_functions.get(output_type, format_functions['stylish'])(diff_tree)
