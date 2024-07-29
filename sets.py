"""st = { 'item1', 'item2', 'item3' }
fruits = {'apple', 'banana', 'mango', 'orange'}
print(len(fruits))

#check if an item exists in the set

if 'banana' in fruits:
    print('banana is in the set')
else:
    print('banana is not in the set')

def check_item(item):
    if item in fruits:
        print(f'{item} is in the set')
    else:
        print(f'{item} is not in the set')

check_item('banana')
check_item('apple')
check_item('cucumber')

def check_item(item):
    return item


while True:
    item = input('Enter the name of the item you want to check ')
    if item in fruits:
        print(check_item(item))
        break
    else:
        print(f'{item} is not in the set. Please try again.')





names = set()

def update_set(item=[]):
    names = set()
    names.update(item)
    return names

lst = ['hello','chief']
print(update_set(lst))


set_list = {'item1','item2','item3'}
set_list.remove('item1')
print(set_list)"""


fruits = {'apple', 'banana', 'mango', 'orange'}
#returned_item = fruits.pop()
#returned_item = fruits.clear()
print(fruits)
del fruits
print(fruits)