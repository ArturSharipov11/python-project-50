def diff_str(diff):
    result = ''
    for key, value in sorted(diff.items()):
        if value[0] == value[1]:
            result += f'  {key}: {value[0]}\n'
        elif value[0] is None:
            result += f'+ {key}: {value[1]}\n'
        elif value[1] is None:
            result += f'- {key}: {value[0]}\n'
        else:
            result += f'- {key}: {value[0]}\n+ {key}: {value[1]}\n'
    return result[:-1]