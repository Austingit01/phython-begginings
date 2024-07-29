"""def check_valid_variable(variable):

    if variable.startswith('_'):
        return True
    if variable[0].isdigit():
        return 'Variable doesn\'t start with a number'
    if variable.startswith('@'):
        return 'Variable name doesn\'t start with a special character'
    
    return variable


print(check_valid_variable('@name'))"""

"""def check_valid_variable2(variable):
    if variable.isidentifier():
        return True
    return False
print(check_valid_variable(spasm66))"""


def check_valid_variable2(variable):
    if variable.isidentifier():
        return True
    return False

while True:
    variable = input('Enter a variable name:')
    if variable == 'exit':
        break
    if check_valid_variable2(variable):
        print(f'The variable {variable} is valid.')
        break
    else:
        print(f'The variable {variable} is not valid')





        