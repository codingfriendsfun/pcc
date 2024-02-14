guests = input("How many guests do you have? ")
guests = int(guests)

if guests > 8:
    print("\nYou will have to wait for a table.")
else:
    print("\nThe table is ready!")