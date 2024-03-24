WHITESPACE = ' '
INDENT = WHITESPACE * 4
PREFIX = {
    'unchanged': f'{INDENT}',
    'added': f'{WHITESPACE * 2}+{WHITESPACE}',
    'deleted': f'{WHITESPACE * 2}-{WHITESPACE}'
}


def get_space(indent, depth):
    return indent * depth


def stringify(value, depth):
    if isinstance(value, str) or isinstance(value, int):
        return value

    elif value is None:
        return 'null'

    elif isinstance(value, dict):
        lines = ["{"]
        for key, val in value.items():
            space = get_space(INDENT, depth + 1)
            lines.append(f"{space}{key}:{WHITESPACE}"
                         f"{stringify(val, depth + 1)}")
        lines.append(f"{INDENT * depth}}}")
        return '\n'.join(lines)


def format_stylish(diff):
    def inner(d, depth=0):
        tree = ['{']
        space = get_space(INDENT, depth)
        for item in d:
            if item['type'] == 'nested':
                children = inner(item['children'], depth + 1)
                tree.append(f"{space}{PREFIX['unchanged']}{item['key']}: "
                            f"{children}")
            elif item['type'] == 'replaced':
                tree.append(f"{space}{PREFIX['deleted']}{item['key']}: "
                            f"{stringify(item['old_value'], depth + 1)}")
                tree.append(f"{space}{PREFIX['added']}{item['key']}: "
                            f"{stringify(item['new_value'], depth + 1)}")
            else:
                tree.append(f"{space}{PREFIX[item['type']]}{item['key']}: "
                            f"{stringify(item['value'], depth + 1)}")
        tree.append(f"{INDENT * depth}}}")
        tree = '\n'.join(tree)
        return tree

    d = diff['children']
    result = inner(d)
    return result


def stylish(diff):
    return format_stylish(diff)
