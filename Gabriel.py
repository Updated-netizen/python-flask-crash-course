tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")

        new_task = {
            "task": task,
            "completed": False
        }

        tasks.append(new_task)

        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")

            for number, task in enumerate(tasks, start=1):

                if task["completed"]:
                    status = "✓"
                else:
                    status = " "

                print(f"{number}. [{status}] {task['task']}")

    # Complete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to complete.")
        else:
            print("\nYour Tasks:")

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task['task']}")

            try:
                task_number = int(
                    input("Enter the task number to complete: ")
                )

                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]["completed"] = True
                    print("Task completed successfully!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # Delete Task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task['task']}")

            try:
                task_number = int(
                    input("Enter the task number to delete: ")
                )

                if 1 <= task_number <= len(tasks):
                    deleted_task = tasks.pop(task_number - 1)
                    print(f"Deleted: {deleted_task['task']}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # Exit
    elif choice == "5":
        print("Goodbye!")
        break

    # Invalid option
    else:
        print("Invalid choice. Please try again.")