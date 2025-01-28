import json
import os 
from tkinter import Tk, Listbox, Button, Entry, END

def load_tasks(filename ="tasks.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

def save_tasks(task_list, filename="tasks.json"):
    with open(filename,"w")as file:
         json.dump(task_list,file)
    
def add_task(task_list,task):
    task_list.append({"task":task,"completed":False})
    print(f"Task'{task}' added!")

def mark_complete(task_list,task_index):
    if 0<= task_index < len(task_list):
        task_list[task_index]["completed"]= True 
        print(f"task '{task_list[task_index]['task']}marked as complete!")
    else:
        print("invalid task index")

def delete_task(task_list,task_index):
    if 0 <= task_index <len(task_list):
        remove_task = task_list.pop(task_index)
        print(f"Task'{remove_task['task']} deleted")
    else:
        print("invalid task index.")

def view_tasks(task_list):
    if not task_list:
        print("no tasks available!")
        return 
    for idx,task in enumerate(task_list):
        status = '✔' if task ['completed'] else 'x'
        print(f"{idx +1}.[{status}]{task['task']}")

def cli_main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Save task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter a task: ")
            add_task(tasks,task)
        elif choice == "3":
            index = int(input("Enter a task number to mark coplete"))-1
            mark_complete(tasks,index)
        elif choice == "4":
            index = int(input("Enter task number to delete:"))-1
            delete_task(tasks,index)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved successfully!")
        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye")
            break
        else:
            print("Invalid choice.")
        
        if __name__ == "__main__":
            print("Welcome to the To-Do List CLI")
            cli_main()
