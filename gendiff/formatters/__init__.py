from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import format_json


class UnknownFormatException(Exception):
    pass


def get_format_name(diff, format_name):
    if format_name == 'stylish' or format_name is None:
        return stylish(diff)
    elif format_name == 'plain':
        return plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    raise UnknownFormatException(f"Unknown format: {format_name}")
