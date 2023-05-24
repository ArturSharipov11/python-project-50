import json


def diff_str(diff):
    result = {}
    for key, value in sorted(diff.items()):
        if isinstance(value[0], dict) and isinstance(value[1], dict):
            result[key] = diff_to_dict(value[0])
        elif value[0] is None:
            result_key = f'+ {key}'
            result[result_key] = value[1]
        elif value[1] is None:
            result_key = f'- {key}'
            result[result_key] = value[0]
        elif value[0] == value[1]:
            result_key = f'  {key}'
            result[result_key] = value[0]
        else:
            result_key = f'- {key}'
            result[result_key] = value[0]
            result_key = f'+ {key}'
            result[result_key] = value[1]
    return result


def over_pr(dict_to_print):
    return json.dumps(dict_to_print, indent=4).replace('"', '').replace("'", '')


def in_plane(diff):
    result = []
    for key, value in sorted(diff.items()):
        if isinstance(value[0], dict) and isinstance(value[1], dict):
            result.append(diff_to_plain(value[0]))
        elif value[0] is None:
            if isinstance(value[1], dict):
                result.append(f"Property '{key}' was added with value: [complex value]")
            else:
                result.append(f"Property '{key}' was added with value: {value[1]}")
        elif value[1] is None:
            result.append(f"Property '{key}' was removed")
        elif value[0] == value[1]:
            result.append(f'Property \'{key}\' was unchanged')
        else:
            if isinstance(value[0], dict):
                result.append(f"Property '{key}' was updated. From [complex value] to {value[1]}")
            else:
                result.append(f"Property '{key}' was updated. From {value[0]} to {value[1]}")
    return '\n'.join(result)