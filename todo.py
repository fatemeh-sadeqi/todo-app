import json

def save_task():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def load_tasks():

    try:
        with open("tasks.json", "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return []

tasks = load_tasks()

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    save_task()
    print("Task added.")

def show_task():
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")

def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.")
        return
    
    show_task()

    try:
        task_number = int(input("Enter task's number: "))
    except ValueError:
        return

    if task_number < 1 or task_number > len(tasks):
        print("Invalid number.")
        return

    tasks.pop(task_number - 1)
    save_task()
    print("task deleted.")


while True:
    print("1- Add task")
    print("2- Show task")
    print("3- Delete task")
    print("4- Exit")

    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a number: ")
        continue

    if num == 1:
        add_task()
    elif num == 2:
        show_task()
    elif num == 3:
        delete_task()
    elif num == 4:
        print("Goodbey")
        break
    else:
        print("Error")
