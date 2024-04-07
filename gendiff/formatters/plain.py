from gendiff.exceptions import UnknownTypeException


def to_str(value):
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


def format_plain(diff, key_path=''):
    lines = []
    children = diff.get('children')
    node_type = diff['type']
    key = diff.get('key', '')
    value = diff.get('value')
    old_value = diff.get('old_value')
    new_value = diff.get('new_value')
    path = f"{key_path}{key}" if key else key_path

    if node_type == 'root':
        lines = map(lambda child: format_plain(child, key_path), children)
        return '\n'.join(lines)

    elif node_type == 'nested':
        result = map(lambda child: format_plain(child, f"{path}."), children)
        lines = filter(lambda x: x, result)
        return '\n'.join(lines)

    elif node_type == 'added':
        lines.append(f"Property '{path}' was added with value: {to_str(value)}")
        return '\n'.join(lines)

    elif node_type == 'deleted':
        lines.append(f"Property '{path}' was removed")
        return '\n'.join(lines)

    elif node_type == 'replaced':
        lines.append(f"Property '{path}' was updated. From {to_str(old_value)} "
                     f"to {to_str(new_value)}")
        return '\n'.join(lines)

    elif node_type == 'unchanged':
        return

    raise UnknownTypeException(f"Unknown type: {node_type}")


def plain(diff):
    return format_plain(diff)
