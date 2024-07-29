Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']

Month = input("Which month are you inquiring for? ")

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
