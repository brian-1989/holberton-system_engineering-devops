#!/usr/bin/python3
""" This script uses the REST API(https://jsonplaceholder.typicode.com)
with the list todos and users, with the id passed in the command line.

"""
import requests
from sys import argv

if __name__ == "__main__":
    url_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    url_users = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()
    task_done = 0
    task_number = 0
    user_name = ""
    for _dict in url_todos:
        if _dict.get("userId") == int(argv[1]) and\
                _dict.get("completed") is True:
            task_done += 1
            task_number += 1
        elif _dict.get("userId") == int(argv[1]) and\
                _dict.get("completed") is False:
            task_number += 1
    for key, value in url_users.items():
        if key == "name":
            user_name = value
    print("Employee {} is done with tasks({}/{}):".format(
        user_name, task_done, task_number))
    for _dict in url_todos:
        if _dict.get("userId") == int(argv[1]) and\
                _dict.get("completed") is True:
            print("\t {}".format(_dict.get("title")))
