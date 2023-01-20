import os

path = 'C:\\xampp\\htdocs\\python\\day-4\\copy.txt'

try:
    os.remove(path)
except FileNotFoundError:
    print('File not found')

#os.rmdir  for directories