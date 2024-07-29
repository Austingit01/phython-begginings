my_dict = {'name':'Austin','skills':['html','Java','C++','Python'],'address':{'state':'Enugu','street':'123 Newlake St','zip code':'20559'}}
print(my_dict['skills'][1])
print(len(my_dict))

"""if my_dict.get('firstname'):
    print('Name exists in the dictionary')

else:
    print('Name does not exist in the dictionary')


my_dict['name'] = 'Bishop'
print(my_dict)

my_dict['skills'].append('Go Lang')
my_dict['skills'].insert(2, 'Go Lang')
print(my_dict)


print('name' in my_dict)

my_dict.pop('name')
print(my_dict.get('name'))
my_dict.popitem()
print(my_dict)"""

#for key in my_dict.keys():
#    print(key)

#for value in my_dict.values():
#    print(value)


for key, mynames in my_dict.items():
    print(f'{key}: {mynames}')

for mynames in my_dict:
    print(mynames)


copied_dict = my_dict.copy()
print(copied_dict)