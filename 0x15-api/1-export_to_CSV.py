#!/usr/bin/python3
""" This script uses the REST API(https://jsonplaceholder.typicode.com)
and create a file in CSV format.

"""
import requests
from sys import argv

if __name__ == "__main__":
    url_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    url_users = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()
    user_name = ""
    for key, value in url_users.items():
        if key == "username":
            user_name = value
    with open("{}.csv".format(argv[1]), 'w') as file:
        for _dict in url_todos:
            if _dict.get("userId") == int(argv[1]):
                file.write('"{}","{}","{}","{}"\n'.format(
                    _dict.get("userId"),
                    user_name, _dict.get("completed"), _dict.get("title")))
