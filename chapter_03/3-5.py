#Invite each guest to dinner
guests = ['tom hiddleston', 'david tennant', 'dame maggie smith']
print(f"Dear {guests[0].title()}, you are invited dinner to talk about acting and Shakespeare and stuff.")
print(f"Dear {guests[1].title()}, you are invited dinner to talk about acting and Shakespeare and stuff.")
print(f"Dear {guests[2].title()}, you are invited dinner to talk about acting and Shakespeare and stuff.")
#David Tennant cannot make it :(
print(f"{guests[1].title()} cannot attend.")
guests[1] = 'sir ian mckellen'
#Invite guests again, replacing David with Sir Ian
print(f"Dear {guests[0].title()}, you are invited dinner to talk about acting and Shakespeare and stuff.")
print(f"Dear {guests[1].title()}, you are invited dinner to talk about acting and Shakespeare and stuff.")
print(f"Dear {guests[2].title()}, you are invited dinner to talk about acting and Shakespeare and stuff.")