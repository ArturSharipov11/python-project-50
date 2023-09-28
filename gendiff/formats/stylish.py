from gendiff.constants import ADDED, REMOVED, NESTED, CHANGED, UNCHANGED


def format_nested(key, value, level):
    return f"{' ' * level * 4}    {key}: {stylish_view(value, level)}"


def format_added(key, value, level):
    return f"{' ' * level * 4}  + {key}: {get_child(value, level)}"


def format_removed(key, value, level):
    return f"{' ' * level * 4}  - {key}: {get_child(value, level)}"


def format_changed(key, old_value, new_value, level):
    lines = []
    lines.append(f"{' ' * level * 4}  - {key}: {get_child(old_value, level)}")
    lines.append(f"{' ' * level * 4}  + {key}: {get_child(new_value, level)}")
    return '\n'.join(lines)


def format_unchanged(key, value, level):
    return f"{' ' * level * 4}    {key}: {get_child(value, level)}"


def stylish_view(diff, level=0):
    lines_to_output = []
    level_indent = ' ' * level * 4

    for top_key, top_value in diff.items():
        type_ = top_value.get('type')
        value = top_value.get('value')
        old_value = top_value.get('from')
        new_value = top_value.get('to')

        if type_ == NESTED:
            lines_to_output.append(format_nested(top_key, value, level))
        elif type_ == ADDED:
            lines_to_output.append(format_added(top_key, value, level))
        elif type_ == REMOVED:
            lines_to_output.append(format_removed(top_key, value, level))
        elif type_ == CHANGED:
            lines_to_output.append(format_changed(top_key, old_value,
                                                  new_value, level))
        elif type_ == UNCHANGED:
            lines_to_output.append(format_unchanged(top_key, value, level))

    return '\n'.join([f"{{{lines_to_output}}}", level_indent])


def get_child(data, level=0, spaces_count=4):
    if not isinstance(data, dict):
        return data
    result = []
    level_indent = ' ' * level * spaces_count
    level += 1
    for key, value in data.items():
        result.append(
            f"{level_indent}    {key}: {get_child(value, level)}"
        )
    return '{\n' + '\n'.join(result) + '\n' + level_indent + '}'
