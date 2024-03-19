def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def build_nested(data1, data2):
    return {
        'type': 'root',
        'children': build_diff(data1, data2)
    }


def build_deleted(data):
    return {
        'type': 'deleted',
        'value': format_value(data)
    }


def build_added(data):
    return {
        'type': 'added',
        'value': format_value(data)
    }


def build_replaced(data1, data2):
    return {
        'type': 'replaced',
        'old_value': format_value(data1),
        'new_value': format_value(data2)
    }


def build_unchanged(data):
    return {
        'type': 'unchanged',
        'value': format_value(data)
    }


def build_diff(data1, data2):
    diff = {}

    for key in sorted(set(data1.keys()) | set(data2.keys())):
        old_value = data1.get(key)
        new_value = data2.get(key)

        if key not in data2:
            diff[key] = build_deleted(old_value)

        elif key not in data1:
            diff[key] = build_added(new_value)

        elif isinstance(old_value, dict) and isinstance(new_value, dict):
            diff[key] = build_nested(old_value, new_value)

        elif old_value != new_value:
            diff[key] = build_replaced(old_value, new_value)

        else:
            diff[key] = build_unchanged(old_value)

    return diff
