INDENT = 4
PREFIX = {
    'other': '    ',
    'added': '  + ',
    'deleted': '  - '
}
REPLACER = " "


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
            lines.append(f"{' ' * depth}{PREFIX['other']}{key}:{REPLACER}"
                         f"{stringify(val, depth + INDENT)}")
        lines.append(f"{' ' * depth}}}")
        return '\n'.join(lines)


def format_stylish(diff, depth=0):
    tree = ['{']
    for key, val in diff.items():
        if val['status'] == 'nested':
            new_value = format_stylish(val['children'], depth + INDENT)
            tree.append(f"{' ' * depth}{PREFIX['other']}{key}: "
                        f"{new_value}")
        elif val['status'] == 'replaced':
            tree.append(f"{' ' * depth}{PREFIX['deleted']}{key}:{REPLACER}"
                        f"{stringify(val['old_value'], depth + INDENT)}")
            tree.append(f"{' ' * depth}{PREFIX['added']}{key}:{REPLACER}"
                        f"{stringify(val['new_value'], depth + INDENT)}")
        else:
            tree.append(f"{' ' * depth}{PREFIX[val['status']]}{key}:{REPLACER}"
                        f"{stringify(val['value'], depth + INDENT)}")
    tree.append(f"{' ' * depth}}}")
    tree = '\n'.join(tree)
    return tree


def stylish(diff):
    return format_stylish(diff)
