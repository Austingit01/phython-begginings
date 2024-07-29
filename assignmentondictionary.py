#question numbers 1-4
dog = {'name':'Llama','color':'Ash','breed':'German Shephard','legs':6,'age':5}
student = {'first_name':'Smart','last_name':'Davis','gender':'male','age':16,'marital_status':'Single','Skills':['Java','SMALLtalk','C++','FORTRAN'],'Country':'Wales','City':'Cardiff','Address':'12 Pyro Avenue'}
lent_of_stud = len(student)
print(f'Lenght of the student dictionary is: {lent_of_stud}')


#question number 5
print(type(student.get('Skills')))


#question number 6
student['Skills'].append('Javascript')
student['Skills'].append('Cobol')
print(student)


#question number 7 - 9
list_of_keys = list(student.keys())
print(list_of_keys)

list_of_values = list(student.values())
print(list_of_values)

student_tuples = list(tuple(student.items()))
print(student_tuples)



#question number 10 - 11
student.popitem()
print(student)

#del dog
print(dog)

