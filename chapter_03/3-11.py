# 3-11. Intentional Error
# originally 3-9
# a script that invites a list of guests to a dinner party and tells you
    # how many people you invited
# but, with an index error

guests = ["Caileigh", "Noelle", "Larissa"]
invite = "you are cordially invited to dinner."

print(f"{guests[0]}, {invite}")
print(f"{guests[1]}, {invite}")
print("Index error:\n")
print(f"{guests[3]}, {invite}")

print(f"You invited {len(guests)} guests to dinner.")