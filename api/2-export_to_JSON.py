#!/usr/bin/python3
""" Export to JSON """
import json
import requests
from sys import argv


if __name__ == "__main__":
    response_users = requests.get('https://jsonplaceholder.typicode.com/users')
    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    employees = response_users.json()
    todos = response_todos.json()
    id = int(argv[1])
    username = ''
    status = ''
    task_title = ''
    user_dict = {}
    tasks_list = []

    for i in employees:
        if id == i.get('id'):
            username = i.get('username')

    for i in todos:
        if id == i.get('userId'):
            tasks_dict = {}
            tasks_title = i.get('title')
            status = i.get('completed')
            tasks_dict["task"] = i.get('title')
            tasks_dict["completed"] = status
            tasks_dict["username"] = username
            tasks_list.append(tasks_dict)
    user_dict[id] = tasks_list

    with open(str(id) + '.json', 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
