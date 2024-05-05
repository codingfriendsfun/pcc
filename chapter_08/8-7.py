def make_album(artist_name, artist_title, song_number=None):
    """

    :param artist_name:
    :param artist_title:
    :param song_number:  (Default value = None)

    """
    album = {
        "name": artist_name,
        "title": artist_title.title(),
    }
    if song_number:
        album["song_number"] = song_number

    return album


# create albums using make_album()
bop = make_album("MGK", "lace up")
flop = make_album("MGK", "binge")
semi_bop = make_album("MGK", "tickets to my downfall", song_number=15)

print(bop)
print(flop)
print(semi_bop)
