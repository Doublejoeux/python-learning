#TO_DO LIST
tasks = []
def add_task():
    tasks.append(input("Enter a task: "))

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        for number, task in enumerate(tasks, start = 1):
            print(f"{number}. {task}")

def remove_task():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        check = input("Number of the task to be removed: ")
        if check.isdigit():
            choice = int(check)
            if choice > len(tasks) or choice < 1:
                print("Invalid")
            else:
                removed = tasks.pop(choice - 1)
                print(f"you removed {removed}")
        else:
            print("Invalid")

def mark_task():
    if len(tasks) == 0:
        print("No tasks available")
    else:    
        check = (input("Number of the task to be marked: "))
        if check.isdigit():
            choice = int(check)
            if choice > len(tasks) or choice < 1:
                print("Invalid")
            else:
                mark = int(choice - 1)
                tasks[mark] = f"{tasks[mark]} [x]"
        else:
            print("Invalid")        

def quit():
    print("End!")

def start():
    options = ["add", "view", "remove", "mark", "quit"]
    choice = input("Add, View, Remove, Mark or Quit: ").lower()
    if choice not in options:
        print("Invalid option")
        return True
    elif choice == "add":
        add_task()
        return True
    elif choice == "view":
        view_tasks()
        return True
    elif choice == "remove":
        remove_task()
        return True
    elif choice == "mark":
        mark_task()
        return True
    else:
        quit()
        return False    

def begin():
    begin = True
    while begin == True:
        choice = start()
        if choice == True:
            begin = True
        else:
            begin = False
             
begin()    