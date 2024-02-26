filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for file in filenames:
    v_file=open(f'../files/{file}', 'w')
    v_file.write('Hello')
    v_file.close() #just a check whether it is working or not