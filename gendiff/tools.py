import os


def norm_file_name(arg):
    return arg.replace('/', os.sep).replace('\\', os.sep)


def get_file_extension(file_name):
    return os.path.splitext(file_name)[1]


def load_file(file_name):
    with open(norm_file_name(file_name)) as _:
        return _.read()


def get_file_content(file_name):
    file_extension = get_file_extension(file_name)
    if file_extension == '.json':
        import json
        return json.loads(load_file(file_name))
    elif file_extension in ('.yml', '.yaml'):
        import yaml
        return yaml.load(load_file(file_name), Loader=yaml.FullLoader)
    else:
        raise ValueError('Unknown file extension')