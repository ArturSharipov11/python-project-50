import json
from collections import defaultdict
from gendiff.tools import map_value, map_stylish
from gendiff.constan import CHANGED, OLD, NEW, ADDED, REMOVED, UNCHANGED, NESTED

def diff_str(diff):
    result = defaultdict(dict)
    for key, value in sorted(diff.items()):
        if value['type'] == CHANGED:
            result[f'- {key}'] = value['value'][OLD]
            result[f'+ {key}'] = value['value'][NEW]
        elif value['type'] == ADDED:
            result[f'+ {key}'] = value['value']
        elif value['type'] == REMOVED:
            result[f'- {key}'] = value['value']
        elif value['type'] == UNCHANGED:
            result[key] = value['value']
        elif value['type'] == NESTED:
            result[key] = diff_str(value['value'])
    return result


def form_stylish(diff):
    to_print = diff_str(diff)

    def stylish(dict_to_stylish, tab='    ', lvl=1):
        result = '{\n'
        for key, value in dict_to_stylish.items():
            if isinstance(value, dict):
                if key.startswith('+') or key.startswith('-'):
                    result += f"{tab * lvl}{map_stylish(key)}: {stylish(value, tab, lvl + 1)}"[2:] + '\n'
                else:
                    result += f"{tab * lvl}{key}: {stylish(value, tab, lvl + 1)}\n"
            else:
                if key.startswith('+') or key.startswith('-'):
                    result += f"{tab * lvl}{map_stylish(key)}: {map_stylish(value)}"[2:] + '\n'
                else:
                    result += f'{tab * lvl}{key}: {map_stylish(value)}\n'
        result += f'{tab * (lvl - 1)}}}'
        return result

    return stylish(to_print)


def form_plain(diff, path=''):
    result = ''
    for key, value in sorted(diff.items()):
        key = f'{path}.{key}' if path else key
        if value['type'] == NESTED:
            result += form_plain(value['value'], f'{key}')
        elif value['type'] == CHANGED:
            result += f"Property '{key}' was updated. " \
                      f"From {map_value(value['value'][OLD])} to {map_value(value['value'][NEW])}\n"
        elif value['type'] == ADDED:
            result += f"Property '{key}' was added with value: {map_value(value['value'])}\n"
        elif value['type'] == REMOVED:
            result += f"Property '{key}' was removed\n"
    return result


def form_json(diff):
    return json.dumps(diff_str(diff), indent=5)
