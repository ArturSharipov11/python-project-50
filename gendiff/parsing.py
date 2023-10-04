import json
import yaml


def parse(data, format):
    FORMATS = {
        'json': json.loads,
        'yaml': yaml.safe_load,
        'yml': yaml.safe_load
    }
    return FORMATS.get(format)(data)


def open_file(file_name):
    with open(file_name, 'r') as file:
        file_data = file.read()
        file_format = file_name.split('.')[-1]
        return file_data, file_format
