import json
import yaml


def get_format(path):
    return path.split('.')[1]


def open_json(path):
    return json.load(open(path))


def open_yaml(path):
    return yaml.safe_load(open(path))


def parse(path):
    format = get_format(path)
    if format == 'yml' or format == 'yaml':
        return open_yaml(path)
    elif format == 'json':
        return open_json(path)
    else:
        raise ValueError('Unknown file extension')