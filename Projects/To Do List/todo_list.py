def print_menu():
    print("Todo List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Completed Tasks")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    
    print("Tasks:")
    for index, task_info in enumerate(tasks, start=1):
        status = "✓" if task_info["completed"] else " "
        print(f"{index}. [{status}] {task_info['task']}")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the index of the task you want to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def remove_completed_tasks(tasks):
    tasks[:] = [task for task in tasks if not task["completed"]]
    print("Completed tasks removed!")

def todo_list_app():
    tasks = []
    while True:
        print_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                mark_task_completed(tasks)
            elif choice == 4:
                remove_completed_tasks(tasks)
            elif choice == 5:
                print("Exiting the Todo List application.")
                break
            else:
                print("Invalid choice. Please choose a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    todo_list_app()
