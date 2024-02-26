user_name=input('Add a new name: ')
file = open('files/members.txt','a')
file.write(user_name)
file.close()