# 9-14. Lottery

from random import choice

source = [3, 7, 9, 5, 2, 27, 42, 53, 78, 91, "A", "B", "F", "J", "P"]

def draw_ticket(source=[]):
    if source:
        ticket = []
        for i in range(4):
            ticket.append(choice(source))
        return ticket
    else:
        return "You did not specify a source.\n"

if __name__ == "__main__":
    print(f"Winning ticket: {draw_ticket(source)}")
