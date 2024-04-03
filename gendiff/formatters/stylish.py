def build_ident(depth, marker=' '):
    return ' ' * (depth * 4 - 2) + f"{marker} "


def stringify(value, depth):
    if isinstance(value, str) or isinstance(value, int):
        return value
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        lines = []
        ident = build_ident(depth)
        for key, val in value.items():
            lines.append(f"{ident}{key}: "
                         f"{stringify(val, depth + 1)}")
            lines_string = "\n".join(lines)
            result = f'{lines_string}\n{build_ident(depth - 1)}'
        return f'{{\n{result}}}'


def format_stylish(diff, depth=0):
    lines = []
    node_type = diff['type']
    children = diff.get('children', [])
    ident = build_ident(depth)

    if node_type == 'root':
        lines = map(lambda node: format_stylish(node, depth + 1), children)
        result = "\n".join(lines)
        return f'{{\n{result}\n}}'

    elif node_type == 'nested':
        lines = map(lambda node: format_stylish(node, depth + 1), children)
        result = "\n".join(lines)
        return f'{ident}{diff["key"]}: {{\n{result}\n{ident}}}'

    elif node_type == 'replaced':
        old_val = stringify(diff['old_value'], depth + 1)
        new_val = stringify(diff['new_value'], depth + 1)
        lines.append(f'{build_ident(depth, "-")}{diff["key"]}: {old_val}')
        lines.append(f'{build_ident(depth,"+")}{diff["key"]}: {new_val}')

    elif node_type == 'deleted':
        val = stringify(diff['value'], depth + 1)
        lines.append(f'{build_ident(depth, "-")}{diff["key"]}: {val}')

    elif node_type == 'added':
        val = stringify(diff['value'], depth + 1)
        lines.append(f'{build_ident(depth, "+")}{diff["key"]}: {val}')

    elif node_type == 'unchanged':
        val = stringify(diff['value'], depth + 1)
        lines.append(f'{ident}{diff["key"]}: {val}')

    else:
        raise ValueError('Incorrect type!')

    return '\n'.join(lines)


def stylish(diff):
    return format_stylish(diff)
