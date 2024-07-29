def is_empty(empty):
    if empty == '':
        return True
    return False

while True:
    details = input('Submit details for your function : ')
    if is_empty(details):
        print('Your function is empty')
    else:
        print(f'You have submitted {details} as your function details')
     


