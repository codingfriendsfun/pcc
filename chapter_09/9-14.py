from random import sample

# Time to gamble with our class representing lottery draws


class Lottery:
    """Model a lottery drawing."""

    def __init__(self, lottery_ticket=[]):
        """Initialize lottery attributes."""

        self.lottery_ticket = lottery_ticket

    def user_ticket(self):
        """Prompt user to submit a lottery sequence."""

        ticket_prompt = "Enter a number between 1-10 or "
        ticket_prompt += "a, b, c, d, f to pick your ticket. "

        submit_ticket = 0

        while submit_ticket != 4:
            new_ticket = []

            get_ticket = input(ticket_prompt)

            new_ticket += get_ticket
            submit_ticket += 1

        return new_ticket

    def draw_ticket(self):
        """Draw a lottery ticket, run until users ticket wins."""

        options = [[num for num in range(1, 10)], "a", "c", "b", "d", "f"]
        draw_ticket = sample(options, 4)

        if self.lottery_ticket == draw_ticket:
            print("Congrats! You win!")

        else:
            print("Better luck next time!")


# Instance of Lottery() representing a persons lottery ticket.
my_ticket = Lottery()

# Prompt user to select their ticket numbers/letters.
my_ticket.user_ticket()

# Draw winning ticket and see if you won.
my_ticket.draw_ticket()
