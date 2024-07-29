def check_data_type():
    list = [1,2,'tool']

    for mylist in list:
        if type(mylist) == str or type(mylist) == float or type(mylist) == bool or type(mylist) == int:
            return 'List contains mixed data types'
        else:
            return type(mylist)
        
   # if type(list[0]) == type(list[1]):
   #     print('they are of the same data type')
   # else:
   #     print('They are not of the same data type')
         

print(check_data_type())
