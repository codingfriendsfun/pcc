motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# modifying an entry
motorcycles[0] = 'ducati'
print(motorcycles)

print() # to add a blank line for readability


# appending values to the end
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

print() # to add a blank line for readability


# use append to build from an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

print() # to add a blank line for readability


# insert entries into a list
motorcycles = ['honda', 'yamaha', 'suzuki'] # not actually necessary
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)

print() # to add a blank line for readability


# delete entries from a list
motorcycles = ['honda', 'yamaha', 'suzuki'] # necessary because we inserted
print(motorcycles)
del motorcycles[0]
print(motorcycles)

print() # to add a blank line for readability


# delete entries from a list from any address
motorcycles = ['honda', 'yamaha', 'suzuki'] # necessary because we inserted
print(motorcycles)
del motorcycles[1]
print(motorcycles)

print() # to add a blank line for readability


# using pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop() # save the popped entry
print(motorcycles)
print(popped_motorcycle)

print() # to add a blank line for readability


# a more complex pop example
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

last_owned = motorcycles.pop() # no index defaults to last entry (-1)
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

print() # to add a blank line for readability


# removing by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati') 
print(motorcycles)

print() # to add a blank line for readability


# can also use variables
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'

motorcycles.remove(too_expensive)  # note: remove only dels first instance
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")