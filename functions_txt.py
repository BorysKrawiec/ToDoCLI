def get_task_txt(file_path="to_do.txt"):
    with open(file_path, 'r')as file:
        # lines = file.readlines()
        # formated_lines = []
        # for line in lines:
        #     line = line.replace('\n', '')
        #     formated_lines.append(line)
        # return formated_lines
        lines = file.readlines()
        if "[" in lines[0] and "]" in lines[0]:
            list_of_tasks = lines[0]
            list_of_tasks = list_of_tasks.replace('[' , '').replace(']' , '').replace('"' , '')
            list_of_tasks = list_of_tasks.split(', ')
            return list_of_tasks
        return [line.replace('\n', '') for line in file.readlines()]


def save_task_txt(task_list, file_path="to_do.txt"):
    with open(file_path, 'w') as file:
        for task in task_list:
            file.write(task + "\n")