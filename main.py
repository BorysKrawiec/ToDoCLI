task_list = []

while True:
    user_action = input("Co chcesz zrobić?")
    if user_action == "add" or user_action == "new":
        new_task = input("Podaj nowe zadanie")
        task_list.append(new_task)
    elif user_action == "show" or user_action == "display":
        for idx, task in enumerate(task_list):
            print(f"{idx+1} - {task}")
    elif user_action == "edit":
        task_number = input("Podaj numer zadania")
        task_number = int(task_number) - 1
        edited_task = input("Podaj nową nazwę zadania")
        task_list[task_number] = edited_task
    elif user_action == "complete":
        completed_task = input("Podaj numer zakończonego zadania")
        completed_task = int(completed_task) - 1
        task_list.pop(completed_task)
    elif user_action == "exit":
        break
    else:
        print("nie ma takiej komendy")
