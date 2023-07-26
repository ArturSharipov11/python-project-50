from gendiff.constan import NESTED, UNCHANGED, CHANGED, OLD, NEW, REMOVED, ADDED

def generate_diff(data1, data2):
    result = {}
    for key, value in data1.items():
        if key in data2:
            if isinstance(value, dict) and isinstance(data2[key], dict):
                descendants = generate_diff(value, data2[key])
                result[key] = {'type': NESTED, 'value': descendants}
            elif value == data2[key]:
                result[key] = {'type': UNCHANGED, 'value': value}
            else:
                result[key] = {'type': CHANGED, 'value': {OLD: value, NEW: data2[key]}}
        else:
            result[key] = {'type': REMOVED, 'value': value}
    for key, value in data2.items():
        if key not in data1:
            result[key] = {'type': ADDED, 'value': value}
    return result
