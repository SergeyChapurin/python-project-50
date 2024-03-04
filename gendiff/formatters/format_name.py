from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def get_format_name(diff, format_name):
    if format_name == 'stylish' or format_name is None:
        return stylish(diff)
    elif format_name == 'plain':
        return plain(diff)
