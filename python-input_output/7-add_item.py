#!/usr/bin/python3
"""A script adding all args to list and save to file"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    main_list = sys.argv[1:]

    if os.path.exists("add_item.json"):
        main_list = load_from_json_file("add_item.json") + main_list

    save_to_json_file(main_list, "add_item.json")


if __name__ == "__main__":
    main()
