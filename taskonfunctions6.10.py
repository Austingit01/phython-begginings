def user_id():
    import random
    import string

    characters = string.ascii_letters
    characters += string.digits
    characters += string.punctuation

    random_user_id = ''

    for i in range(6):
        random_user_id += random.choice(characters)
    

    print(f'Output: {random_user_id}')


user_id()




