def make_album(artist, album):
    """create a dictionary with an arist and an album"""
    new_Album = {'Artist': artist.title(), 'Album':album.title()}
    return new_Album

LincolnPark = make_album('Lincoln Park', 'The End')
Tupac = make_album('Tupac', 'Me against the world')
Beastie = make_album('Beastie Boys', 'Licensed to ill')

print(LincolnPark)
print(Tupac)
print(Beastie)


