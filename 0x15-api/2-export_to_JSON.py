#!/usr/bin/python3
""" This script uses the REST API(https://jsonplaceholder.typicode.com)
and create a file in Json format.

"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    url_users = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()
    user_name = ""
    my_dict_2 = {}
    my_list = []
    for key, value in url_users.items():
        if key == "username":
            user_name = value
    with open("{}.json".format(argv[1]), 'w') as file:
        for _dict in url_todos:
            if _dict.get("userId") == int(argv[1]):
                my_dict_1 = {}
                for key, value in _dict.items():
                    if key == 'title':
                        my_dict_1["task"] = value
                    elif key == 'completed':
                        my_dict_1[key] = value
                my_dict_1["username"] = user_name
                my_list.append(my_dict_1)
        my_dict_2[argv[1]] = my_list
        file.write(json.dumps(my_dict_2))
