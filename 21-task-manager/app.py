
tasks = []

def welcome_message():
  print("Welcome to the Task Management!")
  print("---------------------------------")

def task_options():
  print("\n==== Task Manager =====")
  print("0. Exit from Task Manager")
  print("1. Add New Task")
  print("2. View Task List")
  print("3. Complete Task")
  print("4. Delete the Task")

def user_input():
  try:
    choice = int(input("Enter your choice: [0 - 4]  "))
    
    if choice > 4:
      print("Error: Invalid number. Choose valid number between 0 to 4")
      return False
    
    return choice
  except ValueError:
    print("Error: Invalid number. Choose valid number between 0 to 4")
    return False

# Add new task in the task list
def add_task():
  task = input("\nEnter the task: ")
  tasks.append({"task":task, "completed":False})
  print(f"\nTask '{task}' added successfully!")


# View the Task list
def view_tasks():
  print("\n======= Task List =========")
  if not tasks:
    print("No task added!")
    return
  
  for index, task in enumerate(tasks):
    status = '✓' if task["completed"] else ' '
    print(f"{index+1}. [ {status} ] {task['task']}")
  
  print("===================================")

# Mark task as complete
def mark_task_complete():
  print("===== complete the task =====")

  if not tasks:
    return 
  
  try:
    id = int(input("\nEnter task ID to mark as complete:  "))
    print(len(tasks), id)
    if 1 > id or id > len(tasks):
      print("Error: Invalid task number.")
      return 
    
    task_to_complete = tasks[id - 1]
    task_to_complete["completed"] = True

    print(f"Task '{task_to_complete['task']}' mark as completed.")

  except ValueError:
    print("Error, Invalid task number...")

# Delete the existing task
def delete_task():
  print("===== Delete task =====")

  if not tasks:
    return 
  
  try:
    id = int(input("\nEnter task ID to mark as complete. >  "))
    if 1 > id or id > len(tasks):
      print("Error: Invalid task number.")
      return 
    
    task_to_delete = tasks.pop(id - 1)
    print(f"Task '{task_to_delete['task']}' successfully deleted.")

  except ValueError:
    print("Error, Invalid task number.")


#  Main program
def main():
  welcome_message()

  while True:
    task_options()
  
    choice = user_input()

    if type(choice) == bool and not choice:
      continue

    match choice:
      case 1: 
        add_task()
      case 2: 
        view_tasks()
      case 3:
        mark_task_complete()
      case 4:
        delete_task()
      case _:
        print("\n==== Good Bye =======\n")
        break

main()
  