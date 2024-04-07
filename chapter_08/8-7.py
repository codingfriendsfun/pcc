# 8-7. Album

def make_album(artist_name, album_title, song_count=None):
    album = {
        "Artist Name": artist_name,
        "Album Title": album_title
        }
    if song_count:
        album["Song Count"] = song_count
    return album

print(make_album("Nanna", "How to Start a Garden"))
print(make_album("Maddie Zahm", "Fat Funny Friend"))
print(make_album("Yellowcard", "Ocean Avenue"))

print(make_album("Flamy Grant", "Bible Belt Baby", 10))