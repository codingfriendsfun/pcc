vacations = {}
# Set flag for active poll
poll = True

while poll:
    name = input("What is your name? ")
    vacation = input("If you could travel anywhere, where would you go? ")

    # Store responses
    vacations[name] = vacation

    # Continue poll?
    repeat = input("Do any other responses need to be recorded? (yes/no) ")
    if repeat == 'no':
        poll = False

# Show results
print("\nPOLL RESULTS")
for name, vacation in vacations.items():
    print(f"{name.title()} wants to go to {vacation.title()}.")