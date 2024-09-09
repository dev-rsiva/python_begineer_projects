import json
 
def load_tasks():
    try:
        with open("tasks.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        
def view_tasks(tasks):
    if not tasks:
        print("No task available")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "complete" if(task['status']) else "Incomplete"
            print(f'{index}. {task['title']} - {task['description']} {task['status']}')


def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)


def Add_task(tasks): 
    title = input("title: ")
    description = input("description: ")
    tasks.append({'title': title, 'description': description, 'status': False})
    save_tasks(tasks)

    
def update_task(tasks):

    task_number = int(input('Enter the task number to be updated: ')) - 1
    print(task_number)
    if 0 <= task_number < len(tasks):
        
        new_title = input(f'Enter the new title for the task#{task_number}(Press Enter to keep {tasks[task_number]['title']})')

        if new_title.strip():
            tasks[task_number]['title'] = new_title

        new_description = input(f'Enter the new description for the task#{task_number}(Press Enter to keep {tasks[task_number]['description']})')

        if new_description.strip():
            tasks[task_number]['new_description'] = new_description

        deadline = input(f'Enter the deadline for the task#{task_number}. (Press Enter to skip)')

        if deadline.strip():
            tasks[task_number]['deadline'] = deadline
        
        save_tasks(tasks)


def delete_task(tasks):
    tasknumber = int(input("Enter the task number to delete: ")) - 1
    if 0 < tasknumber < len(tasks):
        tasks.pop(tasknumber)
        save_tasks(tasks)
    
            
        
def main():
    while True:
        tasks = load_tasks()

        print("Welcome to the todo list game")
        print("")
        print("1. view tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Quit") 

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            Add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exit application")
            break
        else:
            print("Invalid choice. Please try again.")

main()
