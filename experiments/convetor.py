import PySimpleGUI as sg
import func_convert

label = sg.Text('Enter Feet: ')
input_box = sg.InputText(key='feet')

label1 = sg.Text('Enter Feet: ')
input_box1 = sg.InputText(key='inches')

convert_button = sg.Button('Convert')
output_val = sg.Text(key='output')

window = sg.Window('Convertor', layout=[[label, input_box],
                                        [label1, input_box1],
                                        [convert_button, output_val]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Convert':
            feet = float(values['feet'])
            inches = float(values['inches'])
            func_convert.converter(feet, inches)
            window['output'].update(value=f'{func_convert.converter(feet, inches)} m', text_color="white")
        case sg.WIN_CLOSED:
            break


window.close()