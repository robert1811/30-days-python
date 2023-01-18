import random

def random_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    password_length = input('type the size of the password: ')

    array = []

    if password_length.isnumeric():
        for i in range(0, int(password_length)):
            array.append(letters[random.randrange(0, len(letters))])
        print(''.join(array))
        random_password()
    else:
        random_password()
random_password()