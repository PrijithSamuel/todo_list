import functions
import PySimpleGUI as sg


label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip='Enter To-do', key='todo') # instead of window output 'window.read()' as ('Add', {0:})-> ('Add', {'to-do':})
add_button = sg.Button('Add')

window = sg.Window('My To-Do App',
                 layout = [[label],[input_box, add_button]],
                 font = ('Helvetica', 20))
while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.set_todos(todos)
        case sg.WIN_CLOSED:
            break


#print(event, values)
window.close()