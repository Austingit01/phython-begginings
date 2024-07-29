def add_number():
    num_one = int(input('Enter your first number here: '))
    num_two = int(input('Enter your second number here: '))
    sum_num = num_one + num_two
    return sum_num


def div_number():
    num_one = int(input('Enter your first number here: '))
    num_two = int(input('Enter your second number here: '))
    quotient = num_one / num_two
    return quotient


def mul_number():
    num_one = int(input('Enter your first number: '))
    num_two = int(input('Enter your second number: '))
    product = num_one * num_two
    return product


def sub_number():
    num_one = int(input('Enter your first number: '))
    num_two = int(input('Enter your second number: '))
    diff = num_one - num_two
    return diff


def main():
    print('1. Addition')
    print('2. Division')
    print('3. Multiplication')
    print('4. Subtraction')

#Experiment
    while True:

        choice = int(input('Enter your choice here: '))

        if choice >= 4:
            print('invalid choice')
            break
        #not main

        if choice == 0:
            print('Are you sure you want to exit?...')
            print('yes, exit\nNo to continue')
            choice = input('Enter your choice: ')
            if choice == 'yes':
                exit()
            else:
                continue
        #if choice == 0:
        #   print('Exiting the program...')
        #   break
            
        if choice == 1:
            print(add_number())
        elif choice == 2:
            print(div_number())
        elif choice == 3:
            print(mul_number())
        elif choice == 4:
            print(sub_number())
       # else:
       #     print('Invalid choice')
            
main()
