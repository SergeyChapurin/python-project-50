from gendiff.exceptions import UnknownTypeException


def build_indent(depth, marker=' '):
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
        ident = build_indent(depth + 1)
        for key, val in value.items():
            lines.append(f"{ident}{key}: "
                         f"{stringify(val, depth + 1)}")
        lines_string = "\n".join(lines)
        return f"{{\n{lines_string}\n{build_indent(depth)}}}"


def format_stylish(diff, depth=0):
    lines = []
    node_type = diff['type']
    children = diff.get('children', [])
    ident = build_indent(depth)

    if node_type == 'root':
        lines = map(lambda node: format_stylish(node, depth + 1), children)
        result = "\n".join(lines)
        return f'{{\n{result}\n}}'

    elif node_type == 'nested':
        lines = map(lambda node: format_stylish(node, depth + 1), children)
        result = "\n".join(lines)
        return f'{ident}{diff["key"]}: {{\n{result}\n{ident}}}'

    elif node_type == 'replaced':
        old_val = stringify(diff['old_value'], depth)
        new_val = stringify(diff['new_value'], depth)
        lines.append(f'{build_indent(depth, "-")}{diff["key"]}: {old_val}')
        lines.append(f'{build_indent(depth, "+")}{diff["key"]}: {new_val}')

    elif node_type == 'deleted':
        val = stringify(diff['value'], depth)
        lines.append(f'{build_indent(depth, "-")}{diff["key"]}: {val}')

    elif node_type == 'added':
        val = stringify(diff['value'], depth)
        lines.append(f'{build_indent(depth, "+")}{diff["key"]}: {val}')

    elif node_type == 'unchanged':
        val = stringify(diff['value'], depth)
        lines.append(f'{ident}{diff["key"]}: {val}')

    else:
        raise UnknownTypeException(f"Unknown type: {node_type}")

    return '\n'.join(lines)


def stylish(diff):
    return format_stylish(diff)
