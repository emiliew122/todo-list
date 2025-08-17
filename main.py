# make a task management system in python
# add tasks, list tasks, edit tasks, delete tasks, save tasks to file, load tasks to file, and exit

# first let's define what a task is.
class task:
    title = ""
    desc = ""
    due = ""
    priority = 1
    status = "Incomplete"

tasks_arr = []

def add_task():
    new = task()
    new.title = input("\nEnter task title: ");
    new.desc = input("Enter task description: ");
    new.due = input("Enter task due (preferably in YYYY-MM-DD format): ")
    new.priority = int(input("Enter task priority (1-3, 1 being Low and 3 being High): "))

    if new.priority > 3 or new.priority < 1: 
        print("Invalid priority level. Defaulting to 1.")
        new.priority = 1

    tasks_arr.append(new)

# then let's make a list_tasks() method where tasks... are listed.
def list_tasks():
    num = 0;
    for task in tasks_arr:
            num += 1
            print(f"\nTask number {num}\nTitle: {task.title}\nDescription: {task.desc}\nDue for the {task.due}")
            
            priority = ""
            match task.priority:
                case 1: priority = "Low"
                case 2: priority = "Medium"
                case 3: priority = "High"
                case _: priority = "I can't code."

            print(f"Priority: {priority}")
            print(f"Task Status: {task.status}")

def delete_tasks():
    show_tasks = input("Do you want to list all tasks? (y/N) ")
    if show_tasks.lower() == "y":
        list_tasks()
    
    task_to_delete = int(input("Enter task number to delete: "))
    task_to_delete -= 1

    tasks_arr.remove(task_to_delete)

def load_tasks():
    filepath = input("\nEnter file name: ")
    line_amount = 0
    try:
        with open(filepath, "r") as file:
            for line in file:
                title, desc, due, priority, status = line.strip().split("|")
                new_task = task()
                new_task.title = title
                new_task.desc = desc
                new_task.due = due
                new_task.priority = int(priority)
                new_task.status = status
                tasks_arr.append(new_task)
                line_amount += 1
        print(f"{line_amount} task(s) loaded from file {filepath}")
    except:
        print("Couldn't open file. Exiting now...")
        quit()

def save_tasks():
    filepath = input("\nEnter file name: ")
    try:
        with open(filepath, "w") as file:
            for t in tasks_arr:
                line = f"{t.title}|{t.desc}|{t.due}|{t.priority}|{t.status}\n"
                file.write(line)
        task_amount = len(tasks_arr)
        print(f"{task_amount} task(s) saved to file {filepath}")
    except:
        print("Couldn't write to file. Exiting now...")
        quit()

# let's do a menu
def menu():
    # hmmmmmm 
    print("\nWelcome to my task management system. What would you like to do? ")
    print("1. Add task\n2. List all tasks\n3. Delete tasks\n4. Save tasks to file\n5. Load tasks from file\n6: Exit")
    choice = int(input())

    match choice:
        case 1:
            add_task()
        case 2:
            list_tasks()
        case 3:
            delete_tasks()
        case 4:
            save_tasks()
        case 5:
            load_tasks()
        case 6:
            quit()
        case _: 
            print("Invalid choice. Exiting now...")
            quit()

while True:
    menu()
