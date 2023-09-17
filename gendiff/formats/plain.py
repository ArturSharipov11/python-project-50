from gendiff.constants import ADDED, NESTED, UNCHANGED, REMOVED, OLD, NEW


def map_plain(value):
    def handle_dict():
        return '[complex value]'

    def handle_bool():
        return str(value).lower()

    def handle_str():
        return f"'{value}'"

    def handle_none():
        return 'null'

    def handle_default():
        return value

    handlers = {
        dict: handle_dict,
        bool: handle_bool,
        str: handle_str,
        type(None): handle_none,
    }
    return handlers.get(type(value), handle_default)()


def map_stylish(string):
    replace = {
        '"': '',
        ',': '',
        '   +': ' +',
        '   -': ' -',
        '"true"': 'true',
        '"false"': 'false',
        '"null"': 'null',
    }
    for key, value in replace.items():
        string = string.replace(key, value)
    return string


def form_plain(diff, path=''):
    def handle_unchanged(key, value):
        return ''

    def handle_changed(key, value):
        return f"Property '{key}' was updated. From {map_plain(value[OLD])} to {map_plain(value[NEW])}\n"

    def handle_added(key, value):
        return f"Property '{key}' was added with value: {map_plain(value[ADDED])}\n"

    def handle_removed(key, value):
        return f"Property '{key}' was removed\n"

    def handle_nested(key, value):
        return form_plain(value[NESTED], f'{key}')


    result = ''
    for key, value in sorted(diff.items()):
        key = f'{path}.{key}' if path else key
        if NESTED in value:
            result += handle_nested(key, value)
        elif OLD in value:
            result += handle_changed(key, value)
        elif UNCHANGED in value:
            result += handle_unchanged(key, value)
        elif ADDED in value:
            result += handle_added(key, value)
        elif REMOVED in value:
            result += handle_removed(key, value)
    return result