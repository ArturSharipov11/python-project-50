from gendiff.eng import get_comparison_resul
from gendiff.parsing import parse, open_file
from gendiff.formats.selection_format import format_select


def generate_diff(first_file, second_file, format_name='stylish'):
    first_data, first_format = open_file(first_file)
    second_data, second_format = open_file(second_file)
    first_dict = parse(first_data, first_format)
    second_dict = parse(second_data, second_format)
    found_diff = get_comparison_resul(first_dict, second_dict)
    selected_format = format_select(format_name)
    return selected_format(found_diff)
