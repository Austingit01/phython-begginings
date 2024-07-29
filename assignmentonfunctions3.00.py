def number():

    while True:
        num = int(input('What is your number? '))

        if num % 2 == 0:
            print('This is an even number')

        else:
            print('This is an odd number')

number()