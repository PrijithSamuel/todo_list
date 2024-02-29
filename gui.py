import functions
import PySimpleGUI as sg
import time

sg.theme('Black') #example
clock = sg.Text('',key='clock') # time.strftime('%b %d, %Y %H:%M:%S')

label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip='Enter To-do',
                         key='todo')  # instead of window output 'window.read()' as ('Add', {0:})-> ('Add', {'to-do':})
add_button = sg.Button('Add', size=(10)) #example
edit_button = sg.Button('Edit')
comp_button = sg.Button('Complete')
exit_button = sg.Button('Exit')
list_box = sg.Listbox(values=functions.get_todos(), key='items', size=[45, 10], enable_events=True)

window = sg.Window('My To-Do App',   # installed Rainbow plug-in
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box ],
                           [edit_button, comp_button, exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    print('Button Event:', event, '\n''Values in Dict', values)
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
            try:
                todos = functions.get_todos()
                edited_todo = values['items'][0]
                new_todo = values['todo'] + '\n'
                index = todos.index(edited_todo)
                todos[index] = new_todo
                functions.set_todos(todos)
                window['items'].update(values=todos)
            except IndexError:
                sg.popup('Please select an item first.', font=('Helvetica', 20))
        case 'items':
            window['todo'].update(value=values['items'][0].strip('\n'))
        case 'Complete':
            try:
                todos = functions.get_todos()
                complete_todo = values['items'][0]
                index = todos.index(complete_todo)
                todos.pop(index)
                functions.set_todos(todos)
                window['items'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select an item first.', font=('Helvetica', 20))
        case 'Exit':
            break
# print(event, values)
window.close()
