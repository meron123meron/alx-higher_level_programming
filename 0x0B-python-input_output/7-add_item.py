#!/usr/bin/python3
"""a script that adds all arguments to a Python list
then save them to a file"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    lists = load_from_json_file("add_item.json")

except FileNotFoundError:
    lists = []
for i in range(1, len(sys.argv)):
    lists.append(sys.argv[i])
save_to_json_file(lists, "add_item.json")
