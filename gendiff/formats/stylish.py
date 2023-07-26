import itertools
from gendiff.constan import ADDED, NESTED, CHANGED, DELETED


def get_stylish(value, replacer=' ', spaces_count=4):  # noqa:C901
    for key, val in value.items():
        if isinstance(val, dict):
            get_stylish(val)
        elif isinstance(val, bool):
            value[key] = str(val).lower()
        elif val is None:
            value[key] = 'null'

    def iter(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * (deep_indent_size - 2)
        current_indent = replacer * depth
        result_list = []
        for key, val in current_value.items():
            if isinstance(val, int):
                result_list.append(
                    f'{replacer * deep_indent_size}{key}: {val}'
                )
            elif 'status' in val:
                if val['status'] == NESTED:
                    result_list.append(
                        f'{replacer * deep_indent_size}'
                        f'{key}: {iter(val["value"], deep_indent_size)}'
                    )
                elif val['status'] == ADDED:
                    result_list.append(
                        f'{deep_indent}+ '
                        f'{key}: {iter(val["value"], deep_indent_size)}'
                    )
                elif val['status'] == DELETED:
                    result_list.append(
                        f'{deep_indent}- '
                        f'{key}: {iter(val["value"], deep_indent_size)}'
                    )
                elif val['status'] == CHANGED:
                    result_list.append(
                        f'{deep_indent}- '
                        f'{key}: {iter(val["value_1"], deep_indent_size)}'
                    )
                    result_list.append(
                        f'{deep_indent}+ '
                        f'{key}: {iter(val["value_2"], deep_indent_size)}'
                    )
                else:
                    result_list.append(
                        f'{deep_indent}  '
                        f'{key}: {iter(val["value"], deep_indent_size)}'
                    )
            else:
                result_list.append(
                    f'{replacer * deep_indent_size}'
                    f'{key}: {iter(val, deep_indent_size)}'
                )
        result = itertools.chain("{", result_list, [current_indent + "}"])
        return '\n'.join(result)

    return iter(value, 0)