def task():
    tasks = []
    print("----WELCOME TO THE TASK MANAGEMENT APP-----")

    total_task = int(input("Enter how many task you want to add ="))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

        print("Today's tasks are\n{tasks}")

        while True:
            operation = int(input("Enter 1-add\n2-update\n3-delete\n4-view\n5-exit/stop/"))
            if operation ==1:
                add = input("Enter task you want to add =")
                task.append(add)
                print(f"Task {add} has been successfully added...")

            elif operation == 2:
                updated_val = input("Enter the task name you want to update =")
                if updated_val in tasks:
                    up = input("Enter new task =")
                    ind = tasks.index(updated_val)
                    tasks[ind] = up
                    print(f"updated task {up}")
        