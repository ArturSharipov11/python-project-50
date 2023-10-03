#!/usr/bin/env python3


from gendiff.main import generate_diff
from gendiff.cli import get_parse


def main():
    args = get_parse()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
