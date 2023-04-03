import json


def get_task_json(file_path="to_do.txt"):
    with open(file_path, 'r')as file:
        return json.loads(file.read())


def save_task_json(task_list, file_path="to_do.txt"):
    with open(file_path, 'w') as file:
        json_list = json.dumps(task_list)
        file.write(json_list)