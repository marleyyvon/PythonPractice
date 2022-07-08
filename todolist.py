def start_todo_list(): 
    """Main function to run the to-do list app."""

    print("Welcome!")
    print("Would you like to")
    print("[A]dd a new task")
    print("[D]elete a task")
    print("[E]dit a task")
    print("[V]iew all tasks")
    print("[Q]uit the program")

    todo_list = []

    while True:
        user_option = input("Choose an option: ")

        if user_option == "A":
            print("What task would you like to add now?")
            new_task=input("> ")
            todo_list.append(new_task)
            print("We added {}.".format(new_task))

        elif user_option == "V":
            for task in todo_list:
                print(task)
        
        elif user_option == "D":
            print("what do you want to delete?")
            task_delete = input(">")

            keep_task = []

            for task in todo_list:
                if task != task_delete:
                    keep_task.append(task)
                todo_list = keep_task
                print ("Deleted task {}.".format(task_delete))
                
        elif user_option == "E":
            print("What task would you like to edit?")
            task_edit = input("> ")

            keep_task = []

            for task in todo_list:
                if task != task_edit:
                    keep_task.append(task)
                    todo_list = keep_task
                    keep_task=(input(">"))
                    todo_list.append(task_edit)
                    print("We edited {}." .format(task_edit))

 
        elif user_option == "Q":
            print("Goodbye!")
            break

        elif user_option == "Q":
            print("Goodbye!")
            break
            
start_todo_list()
