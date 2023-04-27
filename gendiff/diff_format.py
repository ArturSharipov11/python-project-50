#!/usr/bin/env python
import json

def generate_diff(file_path1, file_path2):
    dict1 = json.load(open(file_path1))
    dict2 = json.load(open(file_path2))
    keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    diff_lines = []
    for key in keys:
        if key not in dict1:
            diff_lines.append(f'+ {key}: {json.dumps(dict2[key])}')
        elif key not in dict2:
            diff_lines.append(f'- {key}: {json.dumps(dict1[key])}')
        elif dict1[key] != dict2[key]:
            diff_lines.append(f'- {key}: {json.dumps(dict1[key])}')
            diff_lines.append(f'+ {key}: {json.dumps(dict2[key])}')
        else:
            diff_lines.append(f'  {key}: {json.dumps(dict1[key])}')
    return '{\n' + '\n'.join(diff_lines) + '\n}'

~