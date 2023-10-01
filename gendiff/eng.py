from gendiff.constants import NESTED, UNCHANGED, CHANGED, REMOVED, ADDED


def get_comparison_resul(file1, file2):
    keys = file1.keys() | file2.keys()
    diff = {}
    for key in sorted(keys):
        if key not in file2:
            diff[key] = {'type': REMOVED, 'value': convert_value(file1[key])}
        elif key not in file1:
            diff[key] = {'type': ADDED, 'value': convert_value(file2[key])}
        else:
            val1 = convert_value(file1[key])
            val2 = convert_value(file2[key])
            if isinstance(val1, dict) and isinstance(val2, dict):
                diff[key] = {'type': NESTED, 'value':
                             get_comparison_resul(val1, val2)}
            elif val1 == val2:
                diff[key] = {'type': UNCHANGED, 'value': val1}
            else:
                diff[key] = {'type': CHANGED, 'from': val1, 'to': val2}
    return diff


def convert_value(data):
    if data is None:
        return 'null'
    if isinstance(data, bool):
        return str(data).lower()
    return data
