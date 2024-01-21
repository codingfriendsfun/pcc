# 3-5. Changing Guest List
# a script that invites a list of guests to a dinner party
# but with a declined invite and a new guest

guests = ["Caileigh", "Noelle", "Larissa"]
invite = "you are cordially invited to dinner."

print(f"{guests[0]}, {invite}")
print(f"{guests[1]}, {invite}")
print(f"{guests[2]}, {invite}")

# but someone declined
declined = "Caileigh"
print(f"{declined} can't make it.")
guests.remove(declined)

# invite someone new
guests.append("Rob")

# re-send invites
print(f"{guests[0]}, {invite}")
print(f"{guests[1]}, {invite}")
print(f"{guests[2]}, {invite}")