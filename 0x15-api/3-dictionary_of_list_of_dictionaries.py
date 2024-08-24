#!/usr/bin/python3
'''
A module
'''
import json
import requests
from requests import get
import sys


def to_do_list():
    url = f"https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    to_do = {}
    data = response.json()
    for i in data:
        user_id = i['id']
        user_name = i['username']

        todos_url =\
            f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        response = requests.get(todos_url)
        if response.status_code == 200:
            todos = response.json()
        else:
            print("Failed to retrieve TODO list")
            return

        task = [
            {
                "username": user_name,
                "task": todo['title'],
                "completed": todo['completed'],
            } for todo in todos
        ]
        to_do[f'{user_id}'] = task
    with open("todo_all_employees.json", mode="w", newline="") as jsonfile:
        json.dump(to_do, jsonfile)


if __name__ == "__main__":
    to_do_list()
