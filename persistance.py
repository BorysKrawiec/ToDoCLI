from functions_json import get_task_json, save_task_json
from functions_txt import get_task_txt, save_task_txt
from functions_db import get_task_db, save_task_db


class Persistance:
    def __init__(self, method):
        if method == 'txt':
            self.get_task = get_task_txt
            self.save_task = save_task_txt
        elif method == 'json':
            self.get_task = get_task_json
            self.save_task = save_task_json
        elif method == 'db':
            self.get_task = get_task_db
            self.save_task = save_task_db