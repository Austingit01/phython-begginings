def season():
    Autumn = ['september', 'october', 'november']
    Winter = ['december', 'january', 'february']
    Spring = ['march', 'april', 'may']
    Summer = ['june', 'july', 'august']

    Month = input("Which month are you inquiring for? ").lower()

    if Month in Autumn:
        print('The season is Autumn')
        exit()

    if Month in Winter:
        print('The season is Winter')
        exit()

    if Month in Spring:
        print('The season is Spring')
        exit()

    if Month in Summer:
        print('The season is Summer')
        exit()

    else:
        print(f'Invalid month submitted')
    
season()