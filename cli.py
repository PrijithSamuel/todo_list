from functions import get_todos, set_todos
import time
now=time.strftime('%b %d, %Y %H:%M:%S')
print('it is: ', now)
while True:
    user_action = input('Type add, show, edit, complete and exit: ')
    user_action = user_action.lower().strip()

    if user_action.startswith('add'):
        # if 'add' in user_action: -> add can be any part of line that will create wrong value to be added
        # file=open('files/todo_list.txt', 'r')
        # todos=file.readlines()
        # file.close()

        # with open('files/todo_list.txt', 'r') as file:   # with context manager best part less number of codelines
        # and no need to close the file it automatically does todos = file.readlines()

        todos = get_todos()

        todo = user_action[
               4:] + '\n'  # new line added to manage the data in file, so that it should have line by line data
        todos.append(todo)
        # file=open('files/todo_list.txt', 'w')
        # file.writelines(todos)
        # file.close()
        # with open('files/todo_list.txt', 'w') as file:
        #  file.writelines(todos)

        set_todos(todos)

    elif user_action.startswith('show'):
        # with open('files/todo_list.txt', 'r') as file:   # context manager best part less number of codelines and no need to close the file it automatically does
        #  todos = file.readlines()
        # print(todos)
        todos = get_todos()
        todos = [item.strip('\n') for item in
                 todos]  # list(map(lambda x: x.removesuffix('\n'), todos)) #use of map method
        for index, item in enumerate(todos):
            # item=item.removesuffix('\n') #you can use strip as well -> item.strip('\n')
            print(f"{index + 1}-{item.capitalize()}")
    elif user_action.startswith('edit'):
        try:
            # with open('files/todo_list.txt','r') as file:  # context manager best part less number of codelines and no need to close the file it automatically does
            # todos = file.readlines()
            todos = get_todos()
            number = int(user_action[5:].strip())
            new_todo = input('Enter a new TODO: ')
            old_task = todos[number - 1].strip('\n')
            todos[number - 1] = new_todo + '\n'
            # with open('files/todo_list.txt', 'w') as file:
            #   file.writelines(todos)
            set_todos(todos)
            print(f'Following task is edited: {old_task} to {new_todo.capitalize()}')
        except ValueError:  # except Exception as e:
            print('Provided value is not correct.')

    elif user_action.startswith('complete'):
        try:
            # with open('files/todo_list.txt','r') as file:  # context manager best part less number of codelines and no need to close the file it automatically does
            # todos = file.readlines()
            todos = get_todos()
            number = int(user_action[9:].strip())
            task_completed = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            # with open('files/todo_list.txt', 'w') as file:
            #   file.writelines(todos)
            set_todos(todos)
            print(f'Following task is completed: {task_completed}')
        except (ValueError, IndexError) as e:
            print(e)
    elif 'exit' in user_action:
        break

    else:
        print('Please enter any of these values: Add, Show, Edit, Complete or Exit')

print('Bye!!!')
