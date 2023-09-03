import json
import yaml


def parse(data, data_format):
    if data_format == '.json':
        return json.loads(data)
    elif data_format in ('.yml', '.yaml'):
        return yaml.load(data, Loader=yaml.FullLoader)
    else:
        raise ValueError('Unknown file extension')
    
def open_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()