def make_album(artist_name, album_title, songs=None):
    """Stores album information in a dictionary

    :param artist_name: param album_title:
    :param songs: Default value = None)
    :param album_title: 

    """

    album = {
        "arist": artist_name,
        "album": album_title,
    }

    if songs:
        album["songs"] = songs
    return album


print(
    make_album(
        "Boris Slavov",
        "Baldur's Gate 3 Original Soundtrack",
    )
)

album = make_album("Olivia Rodrigo", "guts", 12)
print(album)

album = make_album("Noah Kahan", "Stick Season")
print(album)
