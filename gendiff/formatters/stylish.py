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

    elif isinstance(value, bool):
        return str(value).lower()

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


def format_stylish(diff, depth=0):
    tree = ['{']
    space = get_space(INDENT, depth)

    for key, val in diff.items():
        if val['type'] == 'root':
            children = format_stylish(val['children'], depth + 1)
            tree.append(f"{space}{PREFIX['unchanged']}{key}: "
                        f"{children}")

        elif val['type'] == 'replaced':
            tree.append(f"{space}{PREFIX['deleted']}{key}:{WHITESPACE}"
                        f"{stringify(val['old_value'], depth + 1)}")
            tree.append(f"{space}{PREFIX['added']}{key}:{WHITESPACE}"
                        f"{stringify(val['new_value'], depth + 1)}")
        else:
            tree.append(f"{space}{PREFIX[val['type']]}{key}:{WHITESPACE}"
                        f"{stringify(val['value'], depth + 1)}")

    tree.append(f"{INDENT * depth}}}")
    tree = '\n'.join(tree)
    return tree


def stylish(diff):
    return format_stylish(diff)
