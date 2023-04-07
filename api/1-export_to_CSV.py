#!/usr/bin/python3
""" Export to CSV """
import csv
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
    task = ''
    to_do_list = []

    for i in employees:
        if id == i.get('id'):
            username = i.get('username')

    with open(str(id) + '.csv', 'w') as csvfile:
        my_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for i in todos:
            if id == i.get('userId'):
                status = i.get('completed')
                task = i.get('title')
                to_do_list.append(id)
                to_do_list.append(username)
                to_do_list.append(status)
                to_do_list.append(task)
                my_writer.writerow(to_do_list)
                to_do_list.clear()
