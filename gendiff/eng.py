def generate_diff(data1, data2):
    result = {}
    for key, value in data1.items():
        if key in data2:
            if value == data2[key]:
                result[key] = [value, value]
            else:
                result[key] = [value, data2[key]]
        else:
            result[key] = [value, None]
    for key, value in data2.items():
        if key not in data1:
            result[key] = [None, value]
    return result