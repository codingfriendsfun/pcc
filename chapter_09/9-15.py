from random import choice
count = 0
winner = False

while winner == False:
    possible_pulls = [1,2,3,4,5,6,7,8,9,10,'r','g','a','v','i']
    my_ticket = [1,7,8,'a']
    winning_numbers =[]
    

    for i in range(4):
        winning_numbers.append(choice(possible_pulls))
    if my_ticket == winning_numbers:
        print('You win!')
        winner = True
    else:
        print(f'You Lost, winning ticket was {winning_numbers} and your ticket was {my_ticket}')
        count += 1
        print(count)
