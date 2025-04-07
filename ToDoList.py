
todo_list = []

def show_menu():
    print("\n TO-DO LIST MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append({"task": task, "completed": False})
    print("✅ Task added!")

def view_tasks():
    if not todo_list:
        print("No tasks found!")
    else:
        print("\n Your Tasks:")
        for i, item in enumerate(todo_list):
            status = "✅" if item["completed"] else "❌"
            print(f"{i + 1}. {item['task']} [{status}]")

def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        todo_list[task_num - 1]["completed"] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid input! Please try again.")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = todo_list.pop(task_num - 1)
        print(f"Removed: {removed['task']}")
    except (IndexError, ValueError):
        print("Invalid input! Please try again.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exiting... Stay productive!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
