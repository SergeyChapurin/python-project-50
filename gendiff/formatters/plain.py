def stringify(value):
    if value is None:
        return "null"
    if isinstance(value, int):
        return value
    if value in ['false', 'true', 'null']:
        return value
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"


def format_plain(diff, path=''):
    lines = []
    for key, val in diff.items():
        property_path = f'{path}{key}'
        if val['status'] == 'added':
            lines.append(f"Property '{property_path}' was added with value: "
                         f"{stringify(val['value'])}")
        elif val['status'] == 'deleted':
            lines.append(f"Property '{property_path}' was removed")
        elif val['status'] == 'replaced':
            lines.append(f"Property '{property_path}' was updated. "
                         f"From {stringify(val['old_value'])} "
                         f"to {stringify(val['new_value'])}")
        elif val['status'] == 'nested':
            value = format_plain(val['children'], f"{property_path}.")
            lines.append(f"{value}")
    return '\n'.join(lines)


def plain(diff):
    return format_plain(diff)
