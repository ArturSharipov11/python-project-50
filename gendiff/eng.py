def generate_diff(data1, data2):
    result = {}
    for key, value in data1.items():
        if key in data2:
            if isinstance(value, dict) and isinstance(data2[key], dict):
                descendants = build_diff_tree(value, data2[key])
                result[key] = {'type': 'nested', 'value': descendants}
            elif value == data2[key]:
                result[key] = {'type': 'unchanged', 'value': value}
            else:
                result[key] = {'type': 'changed', 'value': {'old': value, 'new': data2[key]}}
        else:
            result[key] = {'type': 'removed', 'value': value}
    for key, value in data2.items():
        if key not in data1:
            result[key] = {'type': 'added', 'value': value}
    return result