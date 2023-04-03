from db_manager import *

def get_task_db(file_path="to_do.db"):
    conn = create_connection(file_path)
    create_tasks_table(conn)
    return [val for idx, val in read_whole_table(conn, "tasks")]


def save_task_db(task_list, file_path="to_do.db"):
    conn = create_connection(file_path)
    old_tasks = [val for idx, val in read_whole_table(conn, "tasks")]
    old_tasks_length = len(old_tasks)
    task_list_length = len(task_list)
    if old_tasks_length == task_list_length:
        for i in range(old_tasks_length):
            if old_tasks[i] != task_list[i]:
                update_task(conn, old_tasks[i], task_list[i])
                break
    elif old_tasks_length < task_list_length:
        new_task = set(task_list) - set(old_tasks)
        insert_task(conn, tuple(new_task))
    elif old_tasks_length > task_list_length:
        removed_task = set(old_tasks) - set(task_list)
        delete_task(conn, tuple(removed_task))