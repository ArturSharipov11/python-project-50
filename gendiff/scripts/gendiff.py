#!/usr/bin/env python3
from gendiff.main import gen_diff
from gendiff.cli import parse_args


def main():
    args = parse_args()
    diff = gen_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
