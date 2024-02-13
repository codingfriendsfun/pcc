def make_album(artist_name, album_title, songs=None):
    """Stores album information in a dictionary"""
    album = {
        'arist': artist_name,
        'album': album_title,
    }
    if songs:
        album['songs'] = songs
    return album

while True:
    print("\nPlease share an album with me!")
    print("(enter 'q' at any time to quit)")

    artist = input("What is the artist's name? ")
    if artist == 'q':
        break

    album = input("What is the album's title? ")
    if album == 'q':
        break

    songs = input("How many songs are in the album? (leave blank if unknown) ")
    if songs == 'q':
        break

    recommendation = make_album(artist, album, songs)
    print(recommendation)