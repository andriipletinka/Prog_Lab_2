"""Lab 2 task 2 module"""
import json
from pprint import pprint
import sys

def get_file() -> str:
    """
    Get user input (a path to json file) and return it
    """
    print("Write a path to the file")
    path = input()
    return path


def get_key() -> str:
    """
    Get user input (a key) and exit program if input is empty
    """
    key = input('Choose a key: ')
    print()
    if key == '':
        sys.exit()
    return key


def parse_json(path: str):
    """
    Give a user access to different parts of json file
    """
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    def func(data):
        print('Available keys:', list(data.keys()))
        key = get_key()
        while key not in list(data.keys()):
            print('There are no such keys')
            key = get_key()
        if type(data[key]) == dict:
            print("It is an object\n")
            pprint(data[key])
            print()
            func(data[key])
        else:
            print(data[key])
    func(data)


def main():
    """
    Main function
    """
    path = get_file()
    parse_json(path)


if __name__ == "__main__":
    main()
