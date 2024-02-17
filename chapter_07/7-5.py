ticket_prompt = "\nEnter your age for ticket pricing:\n "
ticket_prompt += "\n(Enter 'quit' to exit)\n"


while True:
    age = input(ticket_prompt)
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age < 13:
            print("Your ticket is $10!")
        else:
            print("Your ticket is $15!")
    else:
        break
                

    
    
    