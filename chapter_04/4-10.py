# this was originally exercise 4-9
# list comprehension cubes

cubes = [num**3 for num in range(1,11)]

print(cubes)

print(f"The first three items in the list are: {cubes[0:3]}")
print(f"Three items from the middle of the list are: {cubes[4:7]}")
print(f"The last three items in the list are: {cubes[-3:10]}")