import os
import json

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Added task: {task}")

def list_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{i}. {task['task']} - {status}")

def mark_task_completed(tasks):
    list_tasks(tasks)
    task_number = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        print(f"Marked task '{tasks[task_number]['task']}' as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    list_tasks(tasks)
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        task = tasks.pop(task_number)
        print(f"Deleted task: {task['task']}")
    else:
        print("Invalid task number.")

def show_menu():
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. List all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
