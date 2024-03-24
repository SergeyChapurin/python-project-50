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


def format_plain(diff):
    def inner(d, key_path=''):
        lines = []

        for item in d:
            path = f"{key_path}{item['key']}"

            if item['type'] == 'added':
                lines.append(f"Property '{path}' was added with value: "
                             f"{stringify(item['value'])}")

            elif item['type'] == 'deleted':
                lines.append(f"Property '{path}' was removed")

            elif item['type'] == 'replaced':
                lines.append(f"Property '{path}' was updated. "
                             f"From {stringify(item['old_value'])} "
                             f"to {stringify(item['new_value'])}")

            elif item['type'] == 'nested':
                value = inner(item['children'], f"{path}.")
                lines.append(f"{value}")

        return '\n'.join(lines)

    d = diff['children']
    return inner(d)


def plain(diff):
    return format_plain(diff)
