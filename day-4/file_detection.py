import os

path = "C:\\xampp\\htdocs\\python\\day-4\\text.txt"

if os.path.exists(path):
    print('That location exists')
    if os.path.isfile(path):
        print('That is a file')
        with open(path) as file:
            print(file.read())
    elif os.path.isdir(path):
        print('That is a directory')
else:
    print('That location doesnt exist')

text = 'Test\ntest\ntest\n'

#a append
#w write
#r read
with open(path, 'a') as file:
    file.write(text)    