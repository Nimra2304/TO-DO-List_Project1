tasks=["Open Python pdf","Read the assignment","Understand the assignment","Execute the assignment","Finish the Assignment"]
running=True
while running:
    print("Do you want to add a task?type either y or n")
    answer=input().strip().lower()
    if answer=="y":
        print("Write your task")
        task_input=input()
        tasks.append(task_input)
    elif answer=="n":
        running=False
    else:
        print("Invalid input ,only type y or n ")
        
for task in tasks:
    print(task)