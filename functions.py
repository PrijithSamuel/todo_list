file_path='files/todo_list.txt'
def get_todos(filepath=file_path):
    with open(filepath,'r') as file_local:  # with context manager best part less number of codelines and no need to close the file it automatically does
        todos_local = file_local.readlines()
    return todos_local


def set_todos(todos_local, filepath=file_path):
    with open(filepath, 'w') as file:
        file.writelines(todos_local)