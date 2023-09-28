import json


def form_json(diff):
    result = [json.dumps(diff, indent=4)]
    return ''.join(result)
