def print_list():
    list = []

    while True:
        your_list_choice = input('What are the items for your list?')

        if len(your_list_choice < 5):
            print('Incomplete items submitted')
        elif len(your_list_choice >= 5):
            list.append(your_list_choice)
            print(f'Your full list: {list}')

print_list()
            
