#task entry
task = []

print("Welcome to task list manager.")
while True:
    
    select_input= input("Select from the following: add, remove, view, exit:")
    #select
    if select_input != "add" and select_input != "remove" and select_input != "view"and select_input != "exit":
            print("Invalid input. Try again.")
            continue
    
    #view
    elif select_input == "view":
        if task:
            print(task)
        else:
             print("There is no tasks recorded.")

    #add
    elif select_input == "add":
        new_item = input("Please enter new task:")
        #check for duplication
        if new_item in task:
            print(f"{new_item} already exist.")
        else:
            print(f"Item {new_item} added.")
            task.append(new_item)

    #remove
    elif select_input == "remove":
        if task:
            remove_item = input("Please enter item to be removed:")
            #chick for existance
            if remove_item in task:
                task.remove(remove_item)
                print(f"Item {remove_item} removed.")
            else:
                print(f"{remove_item} is not in the list")
        else:
             print("There is no tasks recorded.")


    #exit
    elif select_input == "exit":
         break
    
    
  

          




"""

while True:
    user_input = input("Enter a grade (0-100), or 'done' to finish:")
    if user_input.lower() == "done":
        print("Input Terminated")
        break
    try:
        grade = float(user_input)
        if grade < 0 or grade > 100:
            print("Invalid input. Please enter a number between 0 and 100")
            continue
        grades.append(grade)
        print(f"Last input: {grade}")
        print(f"Average :{sum(grades)/len(grades)}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
#save entry
if grades:
    with open("grades.txt","w") as f:
        for g in grades:
            f.write(f"{g}\n")
    print ("Grades saved")
else:
    print ("No grades entered.")
    """