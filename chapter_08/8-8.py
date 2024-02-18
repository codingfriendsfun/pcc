# 8-8. User Albums

def make_album(artist_name, album_title, song_count=None):
    album = {
        "Artist Name": artist_name,
        "Album Title": album_title
        }
    if song_count:
        album["Song Count"] = song_count
    return album

while True:
    name = input("Please enter artist name (or 'quit' to exit): ")

    if name == 'quit':
        break

    album = input("Please enter album name: ")
    print(make_album(name, album))
