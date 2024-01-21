# 3-7. Shrinking Guest List
# a script that invites a list of guests to a dinner party, then uninvites some

guests = ["Caileigh", "Noelle", "Larissa"]
invite = "you are cordially invited to dinner."

print(f"{guests[0]}, {invite}")
print(f"{guests[1]}, {invite}")
print(f"{guests[2]}, {invite}")

print("I found a bigger table.")

# add more people
guests.insert(0, "Christopher")
guests.insert(2, "Rob")
guests.append("Ravi")

# re-send invites
print(f"{guests[0]}, {invite}")
print(f"{guests[1]}, {invite}")
print(f"{guests[2]}, {invite}")
print(f"{guests[3]}, {invite}")
print(f"{guests[4]}, {invite}")
print(f"{guests[5]}, {invite}")

# oops, table delivery snafu
print("Unfortunately, the table won't be here in time. Let's reschedule.")

# uninvite people
message = "I apologize, we'll have to have dinner another time"
print(f"{message}, {guests.pop(0)}.")
print(f"{message}, {guests.pop()}.")
print(f"{message}, {guests.pop()}.")
print(f"{message}, {guests.pop()}.")

# re-invite the remaining folk
invite = "we can still have dinner."
print(f"{guests[0]}, {invite}")
print(f"{guests[1]}, {invite}")

# empty the list
del guests[0]
del guests[0]
# could have also done guests = [], but this is what book asked for
print(guests)
