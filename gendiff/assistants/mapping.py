def map_plain(value):
    def handle_dict():
        return '[complex value]'

    def handle_bool():
        return str(value).lower()

    def handle_str():
        return f"'{value}'"

    def handle_none():
        return 'null'

    def handle_default():
        return value

    handlers = {
        dict: handle_dict,
        bool: handle_bool,
        str: handle_str,
        type(None): handle_none,
    }

    return handlers.get(type(value), handle_default)()


def map_stylish(string):
    replace = {
        '"': '',
        ',': '',
        '   +': ' +',
        '   -': ' -',
        '"true"': 'true',
        '"false"': 'false',
        '"null"': 'null',
    }
    for key, value in replace.items():
        string = string.replace(key, value)
    return string