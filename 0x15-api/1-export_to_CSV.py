#!/usr/bin/python3
'''
A module
'''
import csv
import json
import requests
from requests import get
import sys


def to_do_list(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return
    data = response.json()
    for i in data:
        if i.get('id') == employee_id:
            employee_name = i.get('name')

    todos_url =\
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(todos_url)
    if response.status_code == 200:
        todos = response.json()
    else:
        print("Failed to retrieve TODO list")
        return

    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    print(f"Employee\
 {employee_name} is done with tasks({done_tasks}/{total_tasks}): ")
    for task in completed_tasks:
        print(f"\t {task}")


    with open(f"{employee_id}.csv", mode="w", newline="") as csvfile:
        fieldnames = ["id", "completed", "title"]
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for row in todos:
            writer.writerow([employee_id, employee_name, row['completed'], row['title']])



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            to_do_list(employee_id)
        except ValueError:
            print("Employee ID must be an integer")
