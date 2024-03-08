age = input("What is your age? ")
age = int(age)

if age <3 and age > 0:
    print(f"Since you are {age} the ticket is free")
elif age >= 3 and age < 13:
    print(f"Since you are {age} the ticket is $10")
elif age <= 0:
    print("Oh you.")
else:
    print(f"Since you are {age} the ticket is $15, sucks to be old")




#A move theater charges ticket prices depending on a person's age. IOf a person
#is under the age of 3 the ticket is free, between 3 and 12 ticket is $10, if 
#over 12 the ticket is $15 write a loop where you ask the users age and tell 
#them the cost of the movie