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
#Print the length of the list
print(len(guests))