def get_task(file_path="to_do.txt"):
    with open(file_path, 'r')as file:
        # lines = file.readlines()
        # formated_lines = []
        # for line in lines:
        #     line = line.replace('\n', '')
        #     formated_lines.append(line)
        # return formated_lines
        return [line.replace('\n', '') for line in file.readlines()]


def save_task(task_list, file_path="to_do.txt"):
    with open(file_path, 'w') as file:
        for task in task_list:
            file.write(task + "\n")


task_list = get_task()


while True:
    user_action = input("Co chcesz zrobić?(add, new, show, display, edit, complete, exit)")
    if user_action == "add" or user_action == "new":
        new_task = input("Podaj nowe zadanie")
        task_list.append(new_task)
        save_task(task_list)
    elif user_action == "show" or user_action == "display":
        for idx, task in enumerate(task_list):
            print(f"{idx+1} - {task}")
    elif user_action == "edit":
        task_number = input("Podaj numer zadania")
        try:
            task_number = int(task_number) - 1
            edited_task = input("Podaj nową nazwę zadania")
            task_list[task_number] = edited_task
            save_task(task_list)
        except ValueError:
            print("Oczekiwana była wartość liczbowa")
        except IndexError:
            print("Wybrałeś nieprawidłowy numer zadania")
    elif user_action == "complete":
        completed_task = input("Podaj numer zakończonego zadania")
        try:
            completed_task = int(completed_task) - 1
            task_list.pop(completed_task)
            save_task(task_list)
        except ValueError:
            print("Oczekiwana była wartość liczbowa")
        except IndexError:
            print("Wybrałeś nieprawidłowy numer zadania")
    elif user_action == "exit":
        break
    else:
        print("Nie ma takiej komendy")
