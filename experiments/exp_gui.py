import PySimpleGUI as sg

label = sg.Text('Enter feet: ')
text_field = sg.InputText()
label1 = sg.Text('Enter inches: ')
text_field1 = sg.InputText()
b1 = sg.Button('Convert')

window = sg.Window('Convertor', layout=[[label, text_field], [label1, text_field1], [b1]])
window.read()
window.close()