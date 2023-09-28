from gendiff.constants import NESTED, UNCHANGED, CHANGED, REMOVED, ADDED


def compare_values(key, value1, value2):
    if value1 == value2:
        return {'type': UNCHANGED, 'value': convert_value(value1)}
    else:
        return {'type': CHANGED, 'from': convert_value(value1),
                'to': convert_value(value2)}


def get_comparison_res(file1, file2):
    keys = file1.keys() | file2.keys()
    diff = {}
    for key in sorted(keys):
        if key not in file2:
            diff[key] = {'type': REMOVED, 'value': convert_value(file1[key])}
        elif key not in file1:
            diff[key] = {'type': ADDED, 'value': convert_value(file2[key])}
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            diff[key] = {'type': NESTED,
                         'value': get_comparison_res(file1[key], file2[key])}
        else:
            diff[key] = compare_values(key, file1[key], file2[key])
    return diff


def convert_value(data):
    if data is None:
        return 'null'
    if isinstance(data, bool):
        return str(data).lower()
    return data
