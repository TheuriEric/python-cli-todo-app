import time
import sys
import json
import os
from task import Task
from datetime import datetime

###Checks the user option input##Completed
def choice_valuator(choice):
    if choice not in [1,2,3,4,5]:
        print("Please select an option from 1 to 5 ")
        time.sleep(1)
        return

    if choice == 1: #Adds a new task
        add_tasks()
    elif choice == 2: #Deletes a task by ID
        delete_task()
    elif choice == 3: #Edits tasks e.g statuses
        edit_status()
    elif choice == 4: #List all tasks with statuses
        load_tasks()
    elif choice == 5:
        sys.exit("Bye...")


###Function to add tasks###Complete
def add_tasks(): 
    print("Let's add your task :)")
    time.sleep(0.5)
    def task_details():
        task_id = int(input("Task id: > \n"))
        task_title = input("Enter the task title > \n")
        task_description = input("Add a description > \n")
        def due_date_checker(): 
            while True:
                response = input("Would you like to add a due date? y or n > \n").lower()
                if response not in ["y","n"]:
                    print("Please choose between Y and N...")
                    continue
                elif response == "n":
                    print("No due date selected")
                    return None
                    
                else:
                    try:
                        deadline = input("Enter due date (YYYY-MM-DD)> \n")
                        deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
                        print(f"Due date has been set successfully to {deadline} .")
                        return deadline
                    
                    except ValueError:
                        print("Invalid date format! Use YYYY-MM-DD")
                        continue
        task_due_date = due_date_checker()
        task_status = "Incomplete"
        task = Task(task_id,task_title,task_description,str(task_due_date),task_status).__dict__
        #File section
        filename = "tasks.json"
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, "r") as tasks_file:
                try:
                    task_list = json.load(tasks_file)
                except json.JSONDecodeError:
                    print("Corrupted JSON file.")
                    task_list = []
        else:
                task_list = []
        
        task_list.append(task)
        with open(filename, "w") as file:
            json.dump(task_list,file, indent=4)
        
        file.close()
                

        
        print("Successfully created task")
    task_details()

###Function to show all tasks #Complete
def load_tasks():
    print("Here are all the tasks:\n")
    time.sleep(0.3)
    with open("tasks.json", "r") as tasks_file:
        task_list = json.load(tasks_file)

    #We have already loaded the whole json file, now we want to read it in a well formatted way
    for task in task_list:
        print(f"Task Id: {task['id']}\nTitle: {task['title']}\nDescription: {task['description']}\nDue date: {task['due_date']}\nStatus: {task['completed']}\n")
    
    return task_list

#Function to delete tasks by id
def delete_task():
    new_tasks_list = []
    load_tasks()
    deleted_task = int(input("Enter the task id for the task to be deleted \n>"))
    with open("tasks.json","r") as tasks_list:
        tasks = json.load(tasks_list)
    
    for task in tasks:
        if task['id'] != deleted_task:
            new_tasks_list.append(task)

    with open("tasks.json","w") as tasks_list:
        json.dump(new_tasks_list,tasks_list,indent=4)
        

    print(f"Task: {task['title']} deleted successfully")

#Function to edit the status to either 'complete' or 'incomplete' ###Complete
def edit_status():
    
    tasks_id = []
    load_tasks()
    print("To change status, I will preview all the tasks and you choose which one to modify...\n")
    status_modified = int(input(f"***** Choose the task using it's id. \n > "))
    filename = "tasks.json"
    with open(filename, "r") as tasks_list:
        tasks = json.load(tasks_list)
    for task in tasks:
        print(f"Task id: {task['id']} : {task['title']} : {task['completed']}")
        tasks_id.append(task['id'])

    if status_modified in tasks_id:
        for task in tasks:
            if task['id'] == status_modified:
                if task['completed'] == "Incomplete":
                    new_status = "Completed" 
                elif task['completed'] == "Completed":
                    new_status = "Incomplete"
                else:
                    new_status = "Incomplete"
                
                change_status = input(f"Change status to {new_status}? y or n \n> ").lower()

                if change_status == "y":
                    task['completed'] = new_status
                    print(f"Task status has successfully been changed to {new_status}")
                    with open(filename, "w") as tasks_list:
                        json.dump(tasks, tasks_list, indent=4)
                elif change_status == "n":
                    print(f"The status remains {task['completed']}")
                else:
                    print("Please insert y or n")

    else:
        print(f"Sorry! The task by the id {status_modified} does not exist) :(")

###Id generation and input validation logic is handled here
##Write tests for these functions using unittest in test_utils.py


if __name__ == "__main__":
    edit_status()
