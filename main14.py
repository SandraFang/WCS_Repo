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
    
    
  

          



