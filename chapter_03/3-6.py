# 3-6. More Guests
# a script that invites a list of guests to a dinner party, but with a bigger 
    # table

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