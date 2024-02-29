# 9-15. Lottery Analysis
from importlib import import_module as im # because of '-' in name

MyLottery = im("9-14")
source = MyLottery.source

my_ticket = [3, 7, 53, "B"]
tries = 0
win = False

while win == False:
    tries += 1
    matching_values=0
    winning_ticket = MyLottery.draw_ticket(source)
    for value in winning_ticket:
        if value not in my_ticket:
            break # break out of for loop
        else: 
            matching_values += 1
    if matching_values == 4:
        win = True
    # else continue with next try

print(f"It took {tries} tries to win.")



