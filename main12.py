try:
    with open("diary.txt","a")as f:
        entry=input ("Write your diary entry:")
        f.write(entry+"\n")
except (FileNotFoundError, PermissionError) as e:
    print ("Error:",e)
try:
    with open("diary.txt","r")as f:
        print(f.read())
except (FileNotFoundError, PermissionError) as e:
    print ("Error:",e)