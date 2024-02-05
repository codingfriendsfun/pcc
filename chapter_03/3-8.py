#list of destinatins NOT in alphabetical order
dream_locations = ['Germany', 'Colorado', 'Vancouver', 'Washington', 'Newfoundland']
print("Here is my vacation list in original order.")
print(dream_locations)
#print using sorted()
print("\nHere's my list in alphabetical order.")
print(sorted(dream_locations))
#list is still in correct order
print("\nHere's the original list.")
print(dream_locations)
#use sorted() in reverse
print("\nHere's my list in reverse alphabetical order.")
print(sorted(dream_locations, reverse=True))
#use reverse() to permanently change it
print("\nHere's my list premanently reversed.")
dream_locations.reverse()
print(dream_locations)
#reverse it again
print("\nHere's my list in original order.")
dream_locations.reverse()
print(dream_locations)
#use sort() to put it in permanent alphabetical order
print("\nHere's my list in permanent alphabetical order.")
dream_locations.sort()
print(dream_locations)
#reverse sort()
print("\nHere's my list in permanent reverse alphabetical order.")
dream_locations.sort(reverse=True)
print(dream_locations)