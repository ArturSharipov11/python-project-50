import json
from collections import defaultdict
from gendiff.constants import ADDED, REMOVED, NESTED, UNCHANGED, OLD, NEW
from gendiff.assistants.mapping import map_stylish


def form_stylish(diff):
    def convert_diff_tree_to_dict(diff):
        result = defaultdict(dict)

        def handle_unchanged(key, value):
            result[key] = value[UNCHANGED]

        def handle_changed(key, value):
            result[f'- {key}'] = value[OLD]
            result[f'+ {key}'] = value[NEW]

        def handle_added(key, value):
            result[f'+ {key}'] = value[ADDED]

        def handle_removed(key, value):
            result[f'- {key}'] = value[REMOVED]

        def handle_nested(key, value):
            result[key] = convert_diff_tree_to_dict(value)

        for key, value in sorted(diff.items()):
            if NESTED in value:
                handle_nested(key, value[NESTED])
            elif OLD in value:
                handle_changed(key, value)
            elif UNCHANGED in value:
                handle_unchanged(key, value)
            elif ADDED in value:
                handle_added(key, value)
            elif REMOVED in value:
                handle_removed(key, value)
        return result

    result = json.dumps(convert_diff_tree_to_dict(diff), indent=4)
    return map_stylish(result)