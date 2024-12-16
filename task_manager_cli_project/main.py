from tasks import add_task
from database import initialize_db

def main():
    initialize_db()
    print("Welcome to the Task Manager CLI!")
    while True:
        print("\n1. Add Task")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Task title: ")
            description = input("Task description: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            priority = int(input("Priority (1-5): "))
            add_task(title, description, due_date, priority)
            print("Task added successfully!")
        elif choice == "2":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
