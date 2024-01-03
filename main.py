# # To-do List app using files in python
# importing datetime module to show date and time
from datetime import datetime

# adding a task
def addTask():
     # Opening the file in append mode
     file = open("tasks.txt","a")

     # taking task as user input
     task = input("Enter the task : ")

     # getting current date and time
     current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

     # appending task to the current date and time
     finaltask = current_datetime+" : "+task

     # writing task data into file
     file.write(finaltask+"\n")

     # Closing the file
     file.close()

     # Confirmation message
     print("Task successully added.\n")


def modifyTask(task_number):
    try:
        file = open("tasks.txt", "r")
        tasks = file.readlines()

        # User input for new task
        new_task = input("Enter new task:")

        # Checking whether the task number is valid or out of range
        if task_number < len(tasks) and task_number>=0:
            # Storing data of previous task into a variable
            old_task = tasks[task_number]
            current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            # appending new task with date and time
            tasks[task_number] = current_datetime+" : "+new_task + "\n"

            # Writing contents into file
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            # confirmation message
            print(f"Task '{old_task.strip()}' modified to '{new_task.strip()}' successfully.")
        else:
            print("Invalid task number.")

        # Closing the file
        file.close()
    except FileNotFoundError:
        print("No tasks found.")


def viewTasks():
     try:
          # OPening the file in read mode
          file = open("tasks.txt","r")
          tasks = file.readlines() # reading the contents(tasks)
          print("Your tasks are:")
          print("   Date & Time\t\tTask")
          # Printing one after the other
          for i in range(len(tasks)):
               print(tasks[i])

        # Confirmation message
          print("Tasks have been fetched.\n")
     except FileNotFoundError:
          print("No tasks found.\n")


def deleteTask(task_number):
    try:
        # Opening the file in read mode for reading file contents
        file = open("tasks.txt","r")
        # Reading using readlines() predefined function
        tasks = file.readlines()

        # Checking whether the task number is valid or out of range
        if task_number < len(tasks) and task_number>=0:
            del_task = tasks.pop(task_number)

            # Opening the same file in write mode
            with open("tasks.txt", "w") as file:
                # Rewriting the old contents after popping the deleted element
                file.writelines(tasks)
            
            # Confirmation message
            print(f"Task '{del_task.strip()}' has been deleted from To do list successfully.")
        else:
            # display message if task number is not valid
            print("Invalid task number.")
        
        # Closing the file
        file.close()
    # exception if the file doesn't exists
    except FileNotFoundError:
        print("No tasks found.")


# USER INTERFACE
def main():
    # Declaring the choice to access everywhere in main() and initialize with 0
    choice = 0
    print("\n\n======WELCOME======\n")
    # Running the loop for selecting choices
    while True:
        print("\nTASK MANAGER\n1.Add task\n2.Modify task\n3.Delete task\n4.See tasks\n5.Exit\n")

        # Taking user input
        try:
            choice = int(input())

        # Exception if the choice is not an integer
        except:
                print("Please enter a valid choice.")

        # Checking the choice is valid or not 
        if choice<0 or choice>5:
            print("Please enter a valid choice.")

        # else executes when the choice is valid
        else:
            
            # matching choice to respective functions
            match choice:
                case 1:
                    addTask()

                case 2:
                    viewTasks()
                    task_number = int(input("Enter task number to modify : "))
                    modifyTask(task_number-1)

                case 3:
                    viewTasks()
                    task_number = int(input("Enter task number to delete : "))
                    deleteTask(task_number-1)

                case 4:
                    viewTasks()

                case 5:
                    exit()
                    break
        print("\n\nThank You for using To-do List app.\n")
    
if __name__ == "__main__":
    main()

