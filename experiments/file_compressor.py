import PySimpleGUI as sg
import zip_creator

label=sg.Text('Select files to Compress:')
input_box=sg.InputText(tooltip='Enter files list')
file_button=sg.FilesBrowse('Choose', key='files')

label1=sg.Text('Select Destination Folder:')
input_box1=sg.InputText(tooltip='Enter File Path')
path_button=sg.FolderBrowse('Choose', key='folder')

comp_button=sg.Button('Compress')
output_label = sg.Text(key='output')

window=sg.Window('File Compressor', layout=[[label, input_box, file_button],
                                            [label1, input_box1, path_button],
                                            [comp_button, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    files = values['files'].split(';')
    folder = values['folder']
    zip_creator.make_archive(files,folder)
    window['output'].update(value='Compression completed!')
window.close()