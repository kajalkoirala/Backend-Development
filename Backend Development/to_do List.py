import os

def menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Save and Exit")
    print("5. Exit without saving")
    print("6. Load tasks from file")
    print("7. Clear all tasks")

def add(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added.")

def view(tasks):
    if tasks:
        print("\n--- To-Do List ---")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks found.")

def remove(tasks):
    view(tasks)
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def save(tasks, filename):
    with open(filename, 'w') as f:
        for task in tasks:
            f.write(task + '\n')
    print("Tasks saved.")

def load(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            tasks = f.read().splitlines()  # Load tasks into a list
    else:
        print(f"No existing file found for {filename}. Starting with an empty list.")
    return tasks

def clear(tasks):
    tasks.clear()
    print("All tasks cleared.")

def main():
    filename = "todo_list.txt"
    tasks = load(filename)  # Load tasks when the program starts

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add(tasks)
        elif choice == '2':
            view(tasks)
        elif choice == '3':
            remove(tasks)
        elif choice == '4':
            save(tasks, filename)
            print("Tasks saved. Exiting...")
            break
        elif choice == '5':
            print("Exiting without saving...")
            break
        elif choice == '6':
            tasks = load(filename)  # Reload tasks and update the list
            print("Tasks loaded from file.")
        elif choice == '7':
            clear(tasks)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()



