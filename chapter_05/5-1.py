#write conditional tests, 5 True and 5 False
dog = 'husky'
#true because same text
print("Is dog == 'husky'? I predict True.")
print(dog == 'husky')

#false because different text
print("Is dog == 'russian blue'? I predict False.")
print( dog == 'russian blue')

cat = 'Oliver'
#true because adjusted for case, false when not adjusted
print("\nIs cat == 'oliver'? I predict True.")
print(cat.lower() == 'oliver')
print("Is cat == 'oliver'? I predict False.")
print(cat == 'oliver')

age = 31
#true when same number, false when asked if not equal
print("\nIs age == 31? I predict True.")
print(age == 31)
print("Is age != 31? I predict False.")
print(age != 31)

dogs = ['Antares', 'Chekov', 'Prise', 'Dusty']
#true when in list, false when not in list
print("\nIs Chekov a dog? I predict True.")
print('Chekov' in dogs)
print("Is Rey a dog? I predict False.")
print('Rey' in dogs)