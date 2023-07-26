import json
from gendiff.constan import ADDED, NESTED, CHANGED, DELETED

ADD_COMPLEX = "Property '{s}{k}' was added with value: [complex value]"
ADD_VALUE = "Property '{s}{k}' was added with value: {v}"
DELETE_VALUE = "Property '{s}{k}' was removed"
UPDATE_TO_COMPLEX = "Property '{s}{k}' was updated. From {v} to [complex value]"
UPDATE_TO_VALUE = "Property '{s}{k}' was updated. From [complex value] to {v}"
UPDATE_VALUE_TO_VALUE = "Property '{s}{k}' was updated. From {v_1} to {v_2}"


def get_plain(value):
    for key, val in value.items():
        if isinstance(val, dict):
            get_plain(val)
        elif isinstance(val, bool):
            value[key] = str(val).lower()
        elif val is None:
            value[key] = 'null'

    def iter(current_value, string):
        if not isinstance(current_value, dict):
            return str(current_value)

        result_list = []
        for key, val in current_value.items():
            if isinstance(val, int):
                result_list.append(f'{key}: {val}')
            elif 'status' in val:
                if val['status'] == NESTED:
                    result_list.append(
                        iter(val['value'], string=string + f"{key}.")
                    )
                elif val['status'] == ADDED:
                    if isinstance(val["value"], dict):
                        result_list.append(
                            ADD_COMPLEX.format(s=string, k=key)
                        )
                    else:
                        result_list.append(
                            ADD_VALUE.format(
                                s=string, k=key, v=json.dumps(val["value"])
                            )
                        )
                elif val['status'] == DELETED:
                    result_list.append(
                        DELETE_VALUE.format(s=string, k=key)
                    )
                elif val['status'] == CHANGED:
                    if isinstance(val["value_1"], dict) \
                            and not isinstance(val["value_2"], dict):
                        result_list.append(
                            UPDATE_TO_VALUE.format(
                                s=string, k=key, v=json.dumps(val["value_2"])
                            )
                        )
                    elif isinstance(val["value_2"], dict) \
                            and not isinstance(val["value_1"], dict):
                        result_list.append(
                            UPDATE_TO_COMPLEX.format(
                                s=string, k=key, v=json.dumps(val["value_1"])
                            )
                        )
                    else:
                        result_list.append(
                            UPDATE_VALUE_TO_VALUE.format(
                                s=string, k=key, v_1=json.dumps(val["value_1"]),
                                v_2=json.dumps(val["value_2"])
                            )
                        )
            else:
                result_list.append(
                    iter(val, string=string + f"{key}.")
                )
        string = '\n'.join(result_list)
        return string.replace(
            '''"''', """'""").replace(
            "'false'", "false").replace(
            "'true'", "true").replace(
            "'null'", "null")
    return iter(value, '')