#!/usr/bin/env python3

from gendiff.generate import generate_diff
from gendiff.parse import parse


def main():
    args = parse()
    diff = generate_diff(args.first_file, args.second_file)
    return diff


if __name__ == '__main__':
    main()
