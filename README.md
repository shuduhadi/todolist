# ✅ To-Do List (CLI)

A simple command-line to-do list written in Python. Tasks are saved to a JSON file, so they're still there next time you run it.

## Features

- View all tasks with a ✓ for completed ones
- Add a task
- Mark a task as complete
- Delete a task
- Automatic save to `tasks.json` after every change
- Handles invalid menu choices and non-numeric input

## Run it

Requires Python 3 (standard library only).

```bash
git clone https://github.com/shuduhadi/todolist.git
cd todolist
python todo_list.py
```

## Example

```
=== TODO LIST ===
1. View tasks
2. Add task
3. Mark task as complete
4. Delete task
5. Exit
================

Choose an option (1-5): 2

Enter task name: Finish README
Added: Finish README
```

## What I practised

- Functions and a menu-driven program loop
- Reading and writing JSON files
- Basic error handling with `try` / `except`
