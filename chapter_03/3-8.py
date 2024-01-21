# 3-8. Seeing the World
# a script to list travel locations and practice manipulating the order of lists

locations = ["Dubai", "Castaway Cay", "Iceland", "Perth", "Tokyo"]

print(locations)

# sorted, non-destructive
print(sorted(locations))
print(locations)

print() # printing a blank line for readability


# reverse, destructive
print(locations.reverse())
print(locations)
# again to revert
print(locations.reverse())
print(locations)

print() # printing a blank line for readability


# sort, destructive
print(locations.sort())
print(locations)
# now reverse sort
print(locations.sort(reverse=True))
print(locations)