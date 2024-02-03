# favorite numbers

fav_num = {
    'Alexa' : [7],
    'Ariel' : [4],
    'Caileigh' : [13, 7],
    'Oliver' : [6],
    'Wednesday' : [3]
}

for person, numbers in fav_num.items():
    print(f"{person}'s favorite number(s) are: ")
    for num in numbers:
        print(num)