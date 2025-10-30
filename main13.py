#grade entry
grades = []
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