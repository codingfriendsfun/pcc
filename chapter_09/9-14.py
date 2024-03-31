from random import choice

class Lottery:
    def __init__(self, ticket):
        self.ticket = ticket
        self.possible_pulls = [1,2,3,4,5,6,7,8,9,10,'r','g','a','v','i']
        self.winning_numbers = []
    def lotto(self):
        for _ in range (4):
            self.winning_numbers.append(choice(self.possible_pulls))
        if self.ticket == self.winning_numbers:
            print("You win!")
        else:
            print("Sorry maybe next time!")
            ##uncomment to see tickets its comparing used to check if working
            #print(self.winning_numbers)
            #print(self.ticket)
        

my_ticket = [1,'r','g','a']
my_lotto = Lottery(my_ticket)
my_lotto.lotto()

##can only be run once or the choice starts to use more than 4 numbers so further coding needed
##but this meets the basic requirements and given the timeframe moving to done
## also gives me another interesting thought how do we quickly create 100 instances of this and run them to see if we win in 100 tickets?
## is there a way to make dynamic variable objects coming into play, maybe via input?
##i.e how many tickets do you want to buy? 100 creates 100 tickets and then runs them?