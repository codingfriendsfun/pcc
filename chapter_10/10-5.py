from pathlib import Path ##importing the path info
##defining the variables we need to make this work as well as the path
path = Path('guests.txt')
guest = ''
again = ''
run = True
##Asks for the name and and adds it to the input as well as a line break then 
##prompts for more guests
while run == True:
    guest += input("What is your name? ")
    guest += "\n"
    again = input("Are there any more guests who need to sign? Type N to quit ")
    if again == 'N':
        run = False
##writes the string to the file
path.write_text(guest)
