#Print a list
jedi = ['obi wan kenobi', 'qui gon jinn', 'mace windu', 'anakin skywalker']
print(jedi)
#Print an individual item from that list
print(jedi[0])
#Print it using title() method
print(jedi[1].title())
#Print using [-1]
print(jedi[-2].title())
#Print using an f string
print(f"My favorite Star Wars character is {jedi[1].title()}.")

#Change the value of an item in the list
jedi[3] = 'darth vader'
print(jedi)

#Add an item to the end of the list
jedi.append('luke skywalker')
print(jedi)

#Insert an item into the middle of the list
jedi.insert(4, 'leia organa')
print(jedi)

#Remove an item from the list using delete
del jedi[3]
print(jedi)

#Remove an item using the pop() method and print that popped item
popped_jedi = jedi.pop(1)
print(jedi)
#Use an f statement using a popped variable
print(f"I was very sad when {popped_jedi.title()} died.")

#Remove an item from the list when you know the specific value
jedi.remove('mace windu')
print(jedi)
#Reverse the order of the list
jedi.reverse()
print(jedi)
#Sort the list alphabetically
jedi.sort()
print(jedi)
#Sort the list reverse alphabetically
jedi.sort(reverse = True)
print(jedi)
#Find the length of the list
print(len(jedi))