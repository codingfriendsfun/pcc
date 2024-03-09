







from random import sample

# Time to gamble with our class representing lottery draws
class Lottery:
    """Model a lottery drawing."""

    def __init__(self, lottery_ticket, lottery_attempts=0):
        """Initialize lottery attributes."""

        self.lottery_ticket = lottery_ticket
        self.lottery_attempts = lottery_attempts

    def draw_ticket(self):
        """Draw a lottery ticket, run until users ticket wins."""
        
        options = [[num for num in range(1, 10)], 'k', 'h', 'b', 'w', 'a']
        draw_ticket = sample(options, 4)
        
        while self.lottery_ticket != draw_ticket:
            self.lottery_ticket = sample(options, 4)
            self.lottery_attempts += 1

        print(f"It took {self.lottery_attempts} tries to win the lottery.")


# Instance of Lottery() representing a persons lottery ticket
my_ticket = Lottery([4, 1, 2, 3])

# Initiating draw_ticket method
my_ticket.draw_ticket()