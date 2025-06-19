import time
import json
from task import Task
from datetime import datetime


def add_tasks():
    #global task
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
        task = Task(task_id,task_title,task_description,task_due_date,task_status).__dict__
        with open("tasks.json", "a") as tasks_file:
            json.dump(task, tasks_file,indent=4,default=str)
        tasks_file.close()
        print("Successfully created task ")
    task_details()


def load_tasks():
    print("Here are all the tasks")

def delete_task():
    id_list = None
    load_tasks()
    deleted_task_id = int(input("Enter the task id to delete\n>> "))
    if deleted_task_id in id_list:
        pass
    else:
        print("Please enter a valid task id!")
        delete_task()

    print("Task deleted")

def edit_status():
    task_status = "Complete"
    print("Task status has been edited :)")

def status_marker():
    print("The status has been marked")
###Id generation and input validation logic is handled here
##Write tests for these functions using unittest in test_utils.py