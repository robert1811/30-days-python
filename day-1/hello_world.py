print('Hello world')
name = input('What is your name?: ')

for i in range(len(name)):
    print(name[:i+1])
    if i == len(name) - 1:
        for j in range(-abs(len(name)), 0):
            print(name[:abs(j)])