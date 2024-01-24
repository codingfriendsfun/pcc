#print a list
jedi = ['obi wan kenobi', 'qui gon jinn', 'mace windu', 'anakin skywalker']
print(jedi)
#print an individual item from that list
print(jedi[0])
#print it using title() method
print(jedi[1].title())
#print using [-1]
print(jedi[-2].title())
#print using an f string
print(f"My favorite Star Wars character is {jedi[1].title()}.")
#change the value of an item in the list
jedi[3]='darth vader'
print(jedi)
#add an item to the end of the list
jedi.append('luke skywalker')
print(jedi)
#insert an item into the middle of the list
jedi.insert(4, 'leia organa')
print(jedi)
#remove an item from the list using delete
del jedi[3]
print(jedi)
#remove an item using the pop() method and print that popped item
popped_jedi = jedi.pop(1)
print(jedi)
#use an f statement using a popped variable
print(f"I was very sad when {popped_jedi.title()} died.")
#remove an item from the list when you know the specific value
jedi.remove('mace windu')
print(jedi)
#reverse the order of the list
jedi.reverse()
print(jedi)
#sort the list alphabetically
jedi.sort()
print(jedi)
#sort the list reverse alphabetically
jedi.sort(reverse=True)
print(jedi)
#find the length of the list
print(len(jedi))