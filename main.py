import json
from persistance import Persistance

persistance = Persistance('db')

try:
    task_list = persistance.get_task()
except FileNotFoundError:
    print("Plik który próbujesz wczytać nie istnieje, program stworzy nowy, pusty plik")
    task_list = []
except json.decoder.JSONDecodeError:
    print("Niewłaściwa zawartość pliku")
    task_list = []



while True:
    user_action = input("Co chcesz zrobić?(add, new, show, display, edit, complete, exit) ")
    if user_action == "add" or user_action == "new":
        new_task = input("Podaj nowe zadanie ")
        task_list.append(new_task)
        persistance.save_task(task_list)
    elif user_action == "show" or user_action == "display":
        for idx, task in enumerate(task_list):
            print(f"{idx+1} - {task}")
    elif user_action == "edit":
        task_number = input("Podaj numer zadania ")
        try:
            task_number = int(task_number) - 1
            edited_task = input("Podaj nową nazwę zadania ")
            task_list[task_number] = edited_task
            persistance.save_task(task_list)
        except ValueError:
            print("Oczekiwana była wartość liczbowa")
        except IndexError:
            print("Wybrałeś nieprawidłowy numer zadania")
    elif user_action == "complete":
        completed_task = input("Podaj numer zakończonego zadania ")
        try:
            completed_task = int(completed_task) - 1
            task_list.pop(completed_task)
            persistance.save_task(task_list)
        except ValueError:
            print("Oczekiwana była wartość liczbowa")
        except IndexError:
            print("Wybrałeś nieprawidłowy numer zadania")
    elif user_action == "exit":
        break
    else:
        print("Nie ma takiej komendy")
