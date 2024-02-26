filenames=['a.txt','b.txt','c.txt']
for file in filenames:
    v_file=open(f'../files/{file}','r')
    print(v_file.read())
    v_file.close()