todos=[]

while True:
    user_action = input('Type add, show, edit, complete and exit: ')
    user_action =  user_action.lower().strip()

    match user_action:
        case 'add':
            #file=open('files/todo_list.txt', 'r')
            #todos=file.readlines()
            #file.close()

            with open('files/todo_list.txt', 'r') as file:   # with context manager best part less number of codelines and no need to close the file it automatically does
                todos = file.readlines()

            todo=input('Enter a todo: ' ) + '\n'  # new line added to manage the data in file, so that it should have line by line data
            todos.append(todo)
            #file=open('files/todo_list.txt', 'w')
            #file.writelines(todos)
            #file.close()
            with open('files/todo_list.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('files/todo_list.txt', 'r') as file:   # context manager best part less number of codelines and no need to close the file it automatically does
                todos = file.readlines()
            #print(todos)
            todos=[item.strip('\n') for item in todos]  #list(map(lambda x: x.removesuffix('\n'), todos)) #use of map method
            for index, item in enumerate(todos):
                #item=item.removesuffix('\n') #you can use strip as well -> item.strip('\n')
                print(f"{index+1}-{item}")
        case 'edit':
            with open('files/todo_list.txt',
                      'r') as file:  # context manager best part less number of codelines and no need to close the file it automatically does
                todos = file.readlines()
            number=int(input('Number of TODO to edit: '))
            new_todo=input('Enter a new TODO: ')
            old_task=todos[number-1].strip('\n')
            todos[number-1]= new_todo + '\n'
            with open('files/todo_list.txt', 'w') as file:
                file.writelines(todos)
            print(f'Following task is edited: {old_task} to {new_todo.capitalize()}')
        case 'complete':
            with open('files/todo_list.txt','r') as file:  # context manager best part less number of codelines and no need to close the file it automatically does
                todos = file.readlines()
            number = int(input('Number of TODO to edit: '))
            task_completed=todos[number-1].strip('\n')
            todos.pop(number-1)

            with open('files/todo_list.txt', 'w') as file:
                file.writelines(todos)
            print(f'Following task is completed: {task_completed}')
        case 'exit':
            break

print('Bye!!!')