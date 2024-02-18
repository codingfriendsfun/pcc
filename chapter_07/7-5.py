# 7-5. Movie Tickets

ageInput = ""
age = 0
ticket_price = 0

while ageInput != 'quit':
    ageInput = input("What age person are you buying the ticket for? ")
    if ageInput == 'quit':
        break
    else:
        age = int(ageInput)
        if age < 3:
            ticket_price = 0
        elif age < 12:
            ticket_price = 10
        else:
            ticket_price = 15
    print(f"For a(n) {age} year old, the ticket is {ticket_price} dollars.\n")
        