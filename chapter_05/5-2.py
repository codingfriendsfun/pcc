#test for equality and inequality with strings
print("Testing inequality with strings:")
user = 'Noelle Riley'
print("Is the user 'Noelle Riley'?")
print(user == 'Noelle Riley')
print("Is the user Larissa?")
print(user == 'Larissa Stanton')
#test using lower method
print("Is the user 'noelle riley'?")
print(user.lower() == 'noelle riley')

print("\nNumerical Tests:")
age = 31
#greater than
print("Is age greater than 50? Should be False.")
print(age > 50)
#less than
print("Is age less than 50? Should be True")
print(age < 50)
#greater than or equal to
print("Is age greater than or equal to 21? Should be True")
print(age >= 21)
#less than or equal to
print("Is age less than or equal to 31? Should be True")
print(age <= 31)

#test and/or keywords
print("\nTesting the and and or keywords:")
age_1 = 7 
age_2 = 20
print("Is either person over 18? Should be True.")
print(age_1 >= 18 or age_2 >=18)
print("Are both over 18? Should be False.")
print(age_1 >= 18 and age_2 >=18)

#test if item is or isn't in a list
print("\nTest whether item is in or isn't in a list:")
service_dogs = ['Antares', 'Chekov', 'Prise']
print("Is Antares a service dog? Should be True.")
print('Antares' in service_dogs)
print("Is Dusty a service dog?")
dog = "Dusty"
if dog not in service_dogs:
    print(f"{dog} is not a service dog.")