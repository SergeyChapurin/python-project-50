def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def build_nested(key, data1, data2):
    return {
        'type': 'nested',
        'key': key,
        'children': build_difference(data1, data2)
    }


def build_deleted(key, val):
    return {
        'type': 'deleted',
        'key': key,
        'value': format_value(val)
    }


def build_added(key, val):
    return {
        'type': 'added',
        'key': key,
        'value': format_value(val)
    }


def build_replaced(key, val1, val2):
    return {
        'type': 'replaced',
        'key': key,
        'old_value': format_value(val1),
        'new_value': format_value(val2)
    }


def build_unchanged(key, val):
    return {
        'type': 'unchanged',
        'key': key,
        'value': format_value(val)
    }


def build_difference(data1, data2):
    difference = []

    for key in sorted(set(data1.keys()) | set(data2.keys())):
        old_value = data1.get(key)
        new_value = data2.get(key)

        if key not in data2:
            difference.append(build_deleted(key, old_value))
        elif key not in data1:
            difference.append(build_added(key, new_value))
        elif isinstance(old_value, dict) and isinstance(new_value, dict):
            difference.append(build_nested(key, old_value, new_value))
        elif old_value != new_value:
            difference.append(build_replaced(key, old_value, new_value))
        else:
            difference.append(build_unchanged(key, old_value))

    return difference


def build_diff(data1, data2):
    diff = {
        "type": "root",
        "children": build_difference(data1, data2)
    }
    return diff
