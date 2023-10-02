import json


def form_json(data):
    result = [json.dumps(data, indent=4)]
    return ''.join(result)
