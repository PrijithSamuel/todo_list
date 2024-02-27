import functions
import PySimpleGUI as sg


label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip='Enter To-do', key='todo') # instead of window output 'window.read()' as ('Add', {0:})-> ('Add', {'to-do':})
add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
list_box=sg.Listbox(values=functions.get_todos(), key='items', size=[45, 10], enable_events=True)

window = sg.Window('My To-Do App',
                 layout = [[label],[input_box, add_button],[list_box, edit_button]],
                 font = ('Helvetica', 20))
while True:
    event, values = window.read()
    print('Button Event:', event,'\n''Values in Dict',values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.set_todos(todos)
            window['items'].update(values=todos)
        case sg.WIN_CLOSED:
            break
        case 'Edit':
            todos = functions.get_todos()
            edited_todo=values['items'][0]
            new_todo=values['todo'] + '\n'
            index=todos.index(edited_todo)
            todos[index]=new_todo
            functions.set_todos(todos)
            window['items'].update(values=todos)
        case 'items':
            window['todo'].update(value=values['items'][0])



# print(event, values)
window.close()