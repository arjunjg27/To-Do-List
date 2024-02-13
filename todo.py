import atexit

tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
    saveTasks()

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            deleted_task = tasks.pop(taskToDelete)
            print(f"Task '{deleted_task}' has been removed.")
            saveTasks()
        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input.")

def saveTasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def loadTasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

def exitHandler():
    saveTasks()
    print("Tasks saved. Exiting program.")

if __name__ == "__main__":
    loadTasks()
    atexit.register(exitHandler)
    print("Hello, welcome to 'To Do List App'")
    while True:
        print("Select the following options")
        print("---------------------------------------------------")
        print("1. Add new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        options = input("Choose your choice: ")
        if options == "1":
            addTask()
        elif options == "2":
            deleteTask()
        elif options == "3":
            listTasks()
        elif options == "4":
            break
        else:
            print("Invalid choice.")
