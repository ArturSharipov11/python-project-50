from gendiff.cli import parse_args
from gendiff.eng import generate_diff
from gendiff.tools import get_file_content
from gendiff.out_print import diff_str, over_pr, in_plane
import json


def gen_diff():
    args = parse_args()
    dict1 = get_file_content(args.first_file)
    dict2 = get_file_content(args.second_file)
    diff = generate_diff(dict1, dict2)
    if args.format == 'plain':
        print(in_plane(diff))
    else:
        print(over_pr(diff_str(diff)))


def main():
    gen_diff()


if __name__ == '__main__':
    main()