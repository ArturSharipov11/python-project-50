def generate_diff(data1, data2):
    result = ''
    for key, value in data1.items():
        if key in data2:
            if value == data2[key]:
                result += f'  {key}: {value}\n'
            else:
                result += f'- {key}: {value}\n+ {key}: {data2[key]}\n'
        else:
            result += f'- {key}: {value}\n'
    for key, value in data2.items():
        if key not in data1:
            result += f'+ {key}: {value}\n'
    return result[:-1]