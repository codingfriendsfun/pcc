def make_album(artist_name, artist_title, song_number):
    """Return dictionaries containing album info"""
    album = {'name': artist_name, 'title': artist_title.title(), song_number: song_number}
    return album

while True:
    print("\nTell me about your favorite album:")
    print("(Enter 'quit' at any time to quit)")

    name = input("Artists name: ")
    if name == "quit":
        break
    title = input("Album Title:")
    if title == "quit":
        break
    song_number = input("Number of songs:")
    if song_number == "quit":
        break

    submitted_album = make_album(name, title, song_number)
    print(submitted_album)
