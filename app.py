#Self-made libraries
import utils
#local libraries



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
    while True:
        try:

            choice = int(input("*****CLI TO-DO APP*****\n\nPlease select an option:\n    1. Add a task\n    2. Delete a task\n    3. Change task status\n    4. Show tasks\n    5. Quit\n*****-----*****\n >>Option: "))
            
            utils.choice_valuator(choice)
        except ValueError:
            print("\n\nPlease enter a number from 1 to 5 :(")
        except KeyboardInterrupt:
            print("\n\nQuiting program...")
            exit(0)
        

main()



if __name__ == "__main__":
    main()