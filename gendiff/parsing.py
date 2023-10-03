import json
import yaml


def parse(data, format):
    FORMATS = {
        'json': json.loads,
        'yaml': yaml.safe_load,
        'yml': yaml.safe_load
    }
    return FORMATS.get(format)(data)
