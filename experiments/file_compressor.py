import PySimpleGUI as sg

label=sg.Text('Select files to Compress:')
input_box=sg.InputText(tooltip='Enter files list')
file_button=sg.FilesBrowse('Choose')

label1=sg.Text('Select Destination Folder:')
input_box1=sg.InputText(tooltip='Enter File Path')
path_button=sg.FolderBrowse('Choose')

comp_button=sg.Button('Compress')

window=sg.Window('File Compressor', layout=[[label, input_box, file_button],
                                            [label1, input_box1, path_button],
                                            [comp_button]])

window.read()
window.close()