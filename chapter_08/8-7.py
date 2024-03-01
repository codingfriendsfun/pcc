def make_album(artist_name, artist_title, song_number=None):
    """Return dictionaries containing album info"""
    album = {'name': artist_name, 'title': artist_title.title()}
    if song_number:
        album['song_number'] = song_number
    return album

#create albums using make_album()
bop = make_album('MGK', 'lace up')
flop = make_album('MGK', 'binge')
semi_bop = make_album('MGK', 'tickets to my downfall', song_number=15)

#created a list containing all variables for formatting purposes
bops_and_flops = [bop, flop, semi_bop]

#pulls info from each dictionary inside the bops_and_flops list
for album in bops_and_flops:
    if len(album) == 2:
        print(f"{album['name']} released {album['title']}.")
    else:
        print(f"{album['name']} released {album['title']} with " 
              f"{album['song_number']} songs.")
