#packing and unpacking functions 

#unpacking

def add_numbers(num_1,num_2,num_3,num_4,num_5):
    return num_1 + num_2 + num_3 + num_4 + num_5  

lst = [1,2,3,4,5,]
sum = add_numbers(*lst)
print(sum)

def unpack(*args):
    for num in args:
        print(num * 2)

unpack(1,2,3,4,5,6)

def unpack(*args):
    for num in args:
        print(num)

list = ['hello','world','python','is','fun']
unpack(*list)



lst_2 = [1,2,3,4,5,6,7,8,9]
lst_3 = [1,2,3,4,5]
generalist = [*lst_2, *lst_3]
print(generalist)
print('index', 'items')
for index, general in enumerate(generalist):
    print(' ',index, '-----',general)



