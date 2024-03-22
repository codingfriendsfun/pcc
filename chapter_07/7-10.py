responded = {}
polling_active = True


while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place on earth where would you go? ")

    responded[name] = response

    repeat = input("Would you like to let another persond respond? (yes/no) ")
    if repeat == "no":
        print("\n -- Poll Results --")
        for name, response in responded.items():
            print(
                f"{name} would like to go to {response} for a vacation. That sounds nice"
            )
        polling_active = False
