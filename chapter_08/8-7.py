def make_album(artist, album, songs=1):
    """create a dictionary with an arist and an album"""
    new_Album = {'Artist': artist.title(), 'Album': album.title(),
                 'Songs': songs}
    return new_Album


LincolnPark = make_album('Lincoln Park', 'Solo EP')
Tupac = make_album('Tupac', 'Me against the world', 15)
Beastie = make_album('Daft Punk', 'Da Funk', 3)

print(LincolnPark)
print(Tupac)
print(Beastie)
