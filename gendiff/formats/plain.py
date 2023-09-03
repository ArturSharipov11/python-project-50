from gendiff.constants import ADDED, NESTED, UNCHANGED, REMOVED, OLD, NEW
from gendiff.assistants.mapping import map_plain


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