from gendiff.formats.stylish import stylish_view
from gendiff.formats.plain import flatten
from gendiff.formats.json import form_json


def format_select(format):
    INFERENCE_FORMATS = {
        'stylish': stylish_view,
        'plain': flatten,
        'json': form_json
    }
    output_format = INFERENCE_FORMATS.get(format)
    if not output_format:
        raise ValueError("Invalid file format")
    return output_format
