number = int(input('Enter a positive number : '))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num %  i == 0:
            return False
    return True

if is_prime(number):
    print('This is a prime number')
else:
    print('This is not a prime number')