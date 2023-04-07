#!/usr/bin/python3
""" Gather data from an API """
import requests
from sys import argv


if __name__ == "__main__":
    response_users = requests.get('https://jsonplaceholder.typicode.com/users')
    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    employees = response_users.json()
    todos = response_todos.json()
    id = int(argv[1])
    name = ''
    count = 0
    completed = 0
    uncompleted = 0
    total_tasks = 0
    task_completed = ''
    for i in employees:
        if id == i.get('id'):
            name = i.get('name')
    for i in todos:
        if id == i.get('userId'):
            if i.get('completed') is True:
                completed += 1
            else:
                uncompleted += 1
        total_tasks = uncompleted + completed

    print(f'Employee {name} is done with tasks({completed}/{total_tasks}):')

    for i in todos:
        if id == i.get('userId'):
            if i.get('completed') is True:
                task_completed = i.get('title')
                print(f'\t {task_completed}')
