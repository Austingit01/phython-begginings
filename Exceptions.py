try:
    print(10 + '5')
except:
    print('TypeError: cannot convert interger to a string')


try:
    name = input('Enter your name: ')
    year_of_birth = int(input('Enter your year of birth: '))
    age = 2024 - year_of_birth

    print(f'Hello {name}, you are {age} years old')


except TypeError:
    print('Type Error occurred')

except ValueError:
    print('Invalid Year of Birth')

except ZeroDivisionError:
    print('ZeroDivision Error occured')

except Exception as e:
    print(e)
    
finally:
    print('Finally block executed')