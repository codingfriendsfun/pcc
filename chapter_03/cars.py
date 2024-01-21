cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

print() # adding a blank line for readability


# reverse sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort(reverse=True)
print(cars)

print() # adding a blank line for readability


# temporary operations
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\n Here is the sorted list:")
print(sorted(cars)) #returns a different list rather than modifying the orig

print("\nHere is the original list again:")
print(cars)

print() # adding a blank line for readability


# reversing a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)