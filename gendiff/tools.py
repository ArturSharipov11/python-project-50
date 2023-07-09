import os
from gendiff.parser import parse


def norm_file_name(file_name):
    return file_name.replace('/', os.sep).replace('\\', os.sep)


def get_file_extension(file_name):
    return os.path.splitext(file_name)[1]


def load_file(file_name):
    with open(norm_file_name(file_name)) as _:
        return _.read()


def get_file_content(file_name):
    file_extension = get_file_extension(file_name)
    with open(file_name) as _:
        data = _.read()
    return parse(data, file_extension)


def map_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    else:
        return value


def map_stylish(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value
