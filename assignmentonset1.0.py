Artiste = {'Olamide','Burnaboy','Wizkid','Davido','AyraStarr','Yemialade','Tems'}

def remove_artiste(artist):
    Artiste.remove(artist)
    print(Artiste)
    if Artiste == set():
        print('Exiting the program...')
        exit()
        

    

while True:
    artist = input('Enter the name of the artiste you want to remove: ')
    if artist in Artiste:
        remove_artiste(artist)

    else:
        print(f'{artist} is not in the set. Please try again.')
        