tasks = [] #array 

if __name__ == "__main__":
   ### Create a loop to run the app
   
   def addTask():
       task = input("Please enter a task: ")
       tasks.append(task)
       print(f"Task '{task}' added to the list")
   
   def listTasks():
       if not tasks:
           print("There are no tasks currently")
       else:
           print("Current tasks:")
           for index, task in enumerate(tasks):
               print(f"Task #{index}. {task}")
   
   def deleteTask():
       listTasks()
       try:
           taskToDelete = int(input("Enter the # to delete"))
           if taskToDelete>= 0 and taskToDelete < len(tasks):
               tasks.pop(taskToDelete)
               print(f"Task {taskToDelete} has been removed")
           else:
               print(f"Task {taskToDelete} ")
       except ValueError:
           print("Invalid input")
   
   def editTask():
       listTasks()
       try:
           task_number = int(input("\nEnter the task number to edit it"))
           if 1 <= task_number <= len(tasks):
               new_description = input("Enter the new task description: ")
               tasks[task_number - 1] = new_description 
               print("Task updates successfully")
           else: 
               print("Invalid number")
               
       except ValueError:
           print("Please enter valid number")                                 
   
   print("Welcome to the to do list app! :)") 
   
   while True:
       
       print("\n")
       print("Please select one of the following options")
       print("__________________")
       print("1. Add a new task")
       print("2. Delete a task")
       print("3. List tasks")
       print("4. Edit task")
       print("5. Quit")
       
       choice = input("Enter your choice: ")
       
       if (choice == "1"):
           addTask()
       elif (choice == "2"):
           deleteTask()
       elif (choice =="3"):
           listTasks()
       elif (choice == "4"):
           editTask()
       elif (choice == "5"):
           print("Goodbye")
           break
       else:
           print("Invalid")
          
           
#f in print statement allows embedded variables and expressions into strings for easier/readable formatting

#for index, task in enumerate(tasks) - this line loops through the tasks list with enumerate, which provides both index and task in each iteration

#if else checks condition and runs specific code based on whether the condition is true, try except handles exceptions (runtime error) that may occur during code execution, allowing program to recover without crashing

#except ValueError: catches and handles ValueError exceptions, which occur when operation receives an argument of the right type but an inappropriate value (non-numeric string to an integer). e.g. int(input()) <-- if a string is inputted here then the except would execute because it is supposed to be an input type integer 

       
       