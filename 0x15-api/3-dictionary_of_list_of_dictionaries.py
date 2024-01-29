#!/usr/bin/python3
"""
Extends my Python script to export data in the JSON format
"""
import json
import requests
import sys
if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    todo_all = {user['id']: [{'username': user['username'],
                              'task': task['title'],
                              'completed': task['completed']}
                             for task in todos if task['userId'] == user['id']]
                for user in users}

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todo_all, f)
