import json
import yaml


def parse(data, data_format):
    if data_format == '.json':
        return json.loads(data)
     else:
        return yaml.safe_load(data)
