#Self-made libraries
import utils 



#local libraries
import time

###Will have 
#   1.a main function
#   2.Handle input using input() or argparse but we will use input()
#   3.Implement all required commands and wire them to the logic

##Bonus:
# This section is reserved for those of you who dare! Are you good enough to try 👀 You are required to implement the following 👇

# **Feature**: Add a filter to list only tasks due today

# **Command**: `list --today`

# **Tools**: Use `datetime.date.today()` and the `argparse` module to parse command-line flags

# **Tips**: Format and compare dates properly; test with multiple task dates


def main():
    choice = int(input("*****CLI TO-DO APP*****\n\nPlease select an option:\n    1. Add a task\n    2. Delete a task\n    3. Edit task status\n    4. Show tasks\n\n*****-----*****\n >> Option: "))

    def choice_valuator():
        if choice not in [1,2,3,4]:
            print("Please select an option from 1 to 4 ")
            time.sleep(1)
            main()

    choice_valuator()

    def actions():
        if choice == 1: #Adds a new task
            utils.add_tasks()
        elif choice == 2: #Deletes a task by ID
            utils.delete_task()
        elif choice == 3: #Edits tasks e.g statuses
            utils.edit_status()
        elif choice == 4: #List all tasks with statuses
            utils.load_tasks()
        else:
            main() #Errors
    
    actions()
    
        

    

main()