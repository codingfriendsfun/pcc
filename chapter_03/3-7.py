#Invite each guest to dinner
guests = ['tom hiddleston', 'david tennant', 'dame maggie smith']
print(f"Dear {guests[0].title()}, you are invited dinner to talk about acting and Shakespeare and stuff.")
print(f"Dear {guests[1].title()}, you are invited dinner to talk about acting and Shakespeare and stuff.")
print(f"Dear {guests[2].title()}, you are invited dinner to talk about acting and Shakespeare and stuff.")
#Let them know I found a bigger table
print("I found a bigger table!")
#Add more cool people
guests.insert(0, 'sir ian mckellen')
guests.insert(2, 'dame judy dench')
guests.append('catherine tate')
#Invite all the cool people
print(f"Dear {guests[0].title()}, you are invited to dinner with even more people to talk about acting and Shakespeare and stuff.")
print(f"Dear {guests[1].title()}, you are invited to dinner with even more people to talk about acting and Shakespeare and stuff.")
print(f"Dear {guests[2].title()}, you are invited to dinner with even more people to talk about acting and Shakespeare and stuff.")
print(f"Dear {guests[3].title()}, you are invited to dinner with even more people to talk about acting and Shakespeare and stuff.")
print(f"Dear {guests[4].title()}, you are invited to dinner with even more people to talk about acting and Shakespeare and stuff.")
print(f"Dear {guests[5].title()}, you are invited to dinner with even more people to talk about acting and Shakespeare and stuff.")
#Whoops, I can actually only invite two
print("Unfortunately, I've been informed that only two of you may attend. My bad.")
#Send most embarrassing messages of my life
popped_guests = guests.pop()
print(f"Dear {popped_guests.title()}, unfortunately we have to rescind the invitation to dinner and Shakespeare and stuff. We apologize for the inconvenience.")
popped_guests = guests.pop(2)
print(f"Dear {popped_guests.title()}, unfortunately we have to rescind the invitation to dinner and Shakespeare and stuff. We apologize for the inconvenience.")
popped_guests = guests.pop(0)
print(f"Dear {popped_guests.title()}, unfortunately we have to rescind the invitation to dinner and Shakespeare and stuff. We apologize for the inconvenience.")
popped_guests = guests.pop(1)
print(f"Dear {popped_guests.title()}, unfortunately we have to rescind the invitation to dinner and Shakespeare and stuff. We apologize for the inconvenience.")
#Reprint invitations
print(f"Dear {guests[0].title()}, congratulations! You are still invited to dinner.")
print(f"Dear {guests[1].title()}, congratulations! You are still invited to dinner.")
del guests[0]
del guests[0]
print(guests)