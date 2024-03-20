from pathlib import Path

prompt = "What is your name? "
prompt += "Enter q to quit. "

guest_book = []
name = ""

# while loop for users to input their names
while name != "q":
    name = input(f"{prompt}")
    if name == "q":
        break
    guest_book.append(name)

# Establish path and variable to be written to path
path = Path('./chapter_10/guest.txt')
guests = ''

# Add guest names to variable as a string
for guest in guest_book:
    guests += f"{guest}, "
    
# Write to file
path.write_text(guests)
