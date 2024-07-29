"""def greeting():
    print("Hello World")

#calling a function inside another function
def main():
    greeting()

main()"""
    
"""def get_fullname():
    firstname = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    full_name = firstname + " " + last_name
    print(full_name)

get_fullname()"""

# RETURNING A VALUE TO A FUNCTION
def add_number():
    num_one = int(input("Enter your first value: "))
    num_two = int(input("Enter your second value: "))
    sum = num_one + num_two
    return sum

result = add_number()
result = result + 340
print(result)

#assignment : Write a function that converts from celcius to farenheit . formular = 
#F = (C * 9/5) + 32