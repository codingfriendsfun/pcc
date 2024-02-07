name_1 = 'name'
name_2 = 'eman'
age_1 = 17
age_2 = 25
user_names = ['name', 'noname']
user_ages = [17, 25]

#inequality & equality strings
print(name_1 == 'name')
print(name_2 != 'name')

#using title()
print(name_1.title() == 'Name')
print(name_2.title() != 'name')

#numerical
print(age_1 == 17)
print(age_2 != 17)
print(age_1 < age_2)
print(age_1 > age_2)
print(age_1 <= age_2 )
print(age_1 >= age_2)

#and/or
print("\n")
print(age_1 >= 17 and age_2 >= 17)
print(name_1 == 'enam' or name_2 == "eman")

#item is or isn't in a list
if name_1 in user_names:
    print(name_1)
if name_2 not in user_names:
    print("User not found.")