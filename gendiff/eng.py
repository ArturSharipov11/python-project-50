from gendiff.constants import NESTED, UNCHANGED, CHANGED, REMOVED, ADDED


def get_comparison_results(file1, file2):
    keys = file1.keys() | file2.keys()
    diff = {}
    for key in sorted(keys):
        if key not in file2:
            diff[key] = {'type': REMOVED,
                         'value': convert_value(file1[key])}

        elif key not in file1:
            diff[key] = {'type': ADDED,
                         'value': convert_value(file2[key])}

        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            diff[key] = {'type': NESTED,
                         'value': get_comparison_results(file1[key], file2[key])}  # noqa

        elif file1[key] == file2[key]:
            diff[key] = {'type': UNCHANGED,
                         'value': convert_value(file1[key])}

        elif file1[key] != file2[key]:
            diff[key] = {'type': CHANGED,
                         'from': convert_value(file1[key]),
                         'to': convert_value(file2[key])}
    return diff


def convert_value(data):
    if data is None:
        return 'null'
    if isinstance(data, bool):
        return str(data).lower()
    return data
