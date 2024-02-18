# a script that tells you whether you'll have to wait for a table

party_size = int(input("How large is your dinner party? "))
if party_size > 8:
    print("You will need to wait for a table.")
else:
    print("I can seat you now.")
