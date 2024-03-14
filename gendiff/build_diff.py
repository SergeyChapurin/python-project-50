def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def build_diff(data1, data2):
    diff = {}

    for key in sorted(set(data1.keys()) | set(data2.keys())):
        old_value = data1.get(key)
        new_value = data2.get(key)

        if key not in data2:
            diff[key] = {
                'status': 'deleted',
                'value': format_value(old_value)
            }

        elif key not in data1:
            diff[key] = {
                'status': 'added',
                'value': format_value(new_value)
            }

        elif isinstance(old_value, dict) and isinstance(new_value, dict):
            diff[key] = {
                'status': 'nested',
                'children': build_diff(old_value, new_value)
            }

        elif old_value != new_value:
            diff[key] = {
                'status': 'replaced',
                'old_value': format_value(old_value),
                'new_value': format_value(new_value)
            }

        else:
            diff[key] = {
                'status': 'other',
                'value': format_value(old_value)
            }

    return diff
