import os
from gendiff.parser import parse


def norm_file_name(filename):
    return filename.replace('/', os.sep).replace('\\', os.sep)


def get_file_extension(filename):
    return os.path.splitext(filename)[1]


def load_file(filename):
    with open(norm_file_name(filename)) as file:
        return file.read()


def get_file_content(file_name):
    file_extension = get_file_extension(file_name)
    with open(file_name) as f:
        data = f.read()
    return parse(data, file_extension)
