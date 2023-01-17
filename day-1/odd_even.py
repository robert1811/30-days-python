def odd_even():
    num = input('insert a number: ')
    if int(num) % 2 == 0:
        print(num + ' is even')
    else:
        print(num + ' is odd')
    odd_even()
odd_even()