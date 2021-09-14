#!/usr/bin/python3
""" This script uses the REST API(https://jsonplaceholder.typicode.com)
and create a file in Json format, records all tasks from all employees.

"""
import json
import requests

if __name__ == "__main__":
    url_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    url_users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    user_name = ""
    my_dict_2 = {}
    with open("todo_all_employees.json", 'w') as file:
        for i in range(1, len(url_users) + 1):
            my_list = []
            for _dict in url_users:
                if _dict.get("id") == i:
                    for key, value in _dict.items():
                        if key == "username":
                            user_name = value
            for _dict in url_todos:
                if _dict.get("userId") == i:
                    my_dict_1 = {}
                    for key, value in _dict.items():
                        if key == 'title':
                            my_dict_1["task"] = value
                        elif key == 'completed':
                            my_dict_1[key] = value
                    my_dict_1["username"] = user_name
                    my_list.append(my_dict_1)
            my_dict_2[i] = my_list
        file.write(json.dumps(my_dict_2))
