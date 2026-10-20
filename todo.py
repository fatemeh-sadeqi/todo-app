tasks = []

def add_task():
    print("add task chosen")

def show_task():
    print("show task chosen")

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
        print("Goodby")
        break
    else:
        print("Error")
