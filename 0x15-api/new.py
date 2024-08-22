#!/usr/bin/python3

import requests
import sys
import json

def to_do_list(employee_id):
  url = f"https://jsonplaceholder.typicode.com/users"
  response = requests.get(url)
  if response.status_code != 200:
    print(f"Error: {response.status_code}")
    return
  data = response.json()
  for i in data:
    if i.get('id') == int(employee_id):
      employee_name = i.get('name')


  todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
  response = requests.get(todos_url)
  if response.status_code == 200:
    todos = response.json()
  else:
    print("Failed to retrieve TODO list")
    return

  completed_tasks = [todo['title'] for todo in todos if todo['completed']]

  total_tasks = len(todos)
  done_tasks = len(completed_tasks)

  print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
  for task in completed_tasks:
      print(f"\t {task}")


if __name__ == "__main__":
  if len(sys.argv) != 2:
      print("Usage: python script.py <employee_id>")
  else:
      try:
          employee_id = int(sys.argv[1])
          to_do_list(employee_id)
      except ValueError:
          print("Employee ID must be an integer")
