"""my_tuple = (1,4,5,6,7,3,5,4,0)

print(type(my_tuple))
print(len(my_tuple))
print(my_tuple.count(5))
print(my_tuple[4])
print(my_tuple[0:5])

lst = list(my_tuple)
print(lst)
lst.append(8)
print(lst)

my_list = [1,2,3,4,5,6,7]
my_tuple = tuple(my_list)
print(my_tuple)"""

number_tuple = (2,3,5,7,6,5,9,5.5,8.9,6.0)
fruits = ('banana', 'pineapple', 'orange', 'applee', 'watermelon')
"""print ('applee' in fruits)

def my_fruits():
    for fruit in fruits:
        print(fruit)

my_fruits()"""


my_full_tuple = fruits + number_tuple

for my_full_t in my_full_tuple:
    if type(my_full_t) == str:
        print(my_full_t.upper())

    if isinstance(my_full_t, str):
        print(my_full_t.lower())

    if type(my_full_t) == int:
        print(my_full_t * 10)

    if type(my_full_t) == float:
        print(my_full_t * 100)


#del fruits
#print(fruits)


#Create a tuple containing the name of your brothers and sisters. How many siblings do you have? Modify the tuple and add the name of your mother and father and assign to family members.