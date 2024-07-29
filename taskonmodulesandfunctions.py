from datetime import datetime


def hello_current_time():
    Name = input('What is your name? ')
    current_time = datetime.now().hour

    if current_time < 12:
        print(f'Good morning {Name}')

    elif current_time >= 12:
        print(f'Good afternoon {Name}')

    elif current_time >= 17:
        print(f'Good evening {Name}')

    elif current_time >= 20:
        print(f'Goodnight {Name}')


hello_current_time()