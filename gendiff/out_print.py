import json


def diff_str(diff):
    result = {}
    for key, value in sorted(diff.items()):
        if isinstance(value[0], dict) and isinstance(value[1], dict):
            result[key] = diff_str(value[0])
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


def over_pr(to_print):
    return json.dumps(to_print, indent=4).replace('"', '').replace("'", '')