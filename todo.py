tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def show_task():
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")
    

while True:
    print("1- Add task")
    print("2- Show task")
    print("3- Exit")

    num = int(input("Enter a number: "))

    if num == 1:
        add_task()
    elif num == 2:
        show_task()
    elif num == 3:
        print("Goodbey")
        break
    else:
        print("Error")
