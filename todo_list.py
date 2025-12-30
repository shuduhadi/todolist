import json
import os

def display_menu():
    print('\n=== TODO LIST ===')
    print('1. View tasks')
    print('2. Add task')
    print('3. Mark task as complete')
    print('4. Delete task')
    print('5. Exit')
    print('================')

def view_tasks(tasks):
    if not tasks:
        print('\nNo tasks yet!')
        return
    
    print('\nYour tasks')
    for i, task in enumerate(tasks,1):
        status = '✓' if task['completed'] else ' '
        print(f"{i}. [{status}] {task['name']}")

def add_task(tasks):
    task_name = input('\nEnter task name: ')
    tasks.append({'name': task_name, 'completed': False})
    print(f"Added: {task_name}")

def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input('\nEnter task number to mark complete: '))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print(f"Marked '{tasks[task_num - 1]['name']}' as complete!")
        else:
            print('Invalid task number!')
    except ValueError:
        print('Please enter a valid number!')

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input('\nEnter task number to delete: '))
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            print(f"Deleted: {deleted['name']}")
    except ValueError:
        print('Please enter a valid number!')

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump(tasks, f, indent=2)

def load_tasks(filename= 'tasks.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input('\nChoose an option (1-5): ')
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == '5':
            print('\nGoodbye!')
            break
        else:
            print('\nInvalid choice! Please choose 1-5')

if __name__ == '__main__':
    main()
