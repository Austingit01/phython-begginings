def fullname(firstname, lastname):
    firstname = input('Enter your firstname: ')
    lastname = input('Enter your surname: ')
    Sp = firstname.split()
    firstname_initial = Sp[0][0]
    print(f'Your fullname is {firstname_initial}.{lastname}@gmail.com')

fullname(firstname=(), lastname=())




