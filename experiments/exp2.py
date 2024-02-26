contents=['All carrots are to be sliced longitudinally.','The carrots were reportedly sliced.','The slicing process was well presented.']
filenames=['doc.txt','report.txt','presentation.txt']

# for i in range(len(filenames)):
 #   k='files/' + filenames[i]
 #   #file=file + i
  #  file=open(k,'w')
  #  file.writelines(contents[i])
 #   file.close()

for content, filename in zip(contents, filenames):
    file=open(f'files/{filename}', 'w')
    file.writelines(content)
    file.close()
