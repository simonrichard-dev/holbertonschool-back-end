#!/usr/bin/python3
""" Dictionary of list of dictionaries """
import json
import requests
from sys import argv


if __name__ == "__main__":
    response_users = requests.get('https://jsonplaceholder.typicode.com/users')
    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    employees = response_users.json()
    todos = response_todos.json()
    username = ''
    status = ''
    task_title = ''
    user_dict = {}

    for i in employees:
        username = i.get('username')
        id = i.get('id')
        tasks_list = []

        for j in todos:
            if id == j.get('userId'):
                tasks_dict = {}
                tasks_title = j.get('title')
                status = j.get('completed')
                tasks_dict["task"] = j.get('title')
                tasks_dict["completed"] = status
                tasks_dict["username"] = username
                tasks_list.append(tasks_dict)
        user_dict[id] = tasks_list

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
