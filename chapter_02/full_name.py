first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print (full_name)

# These strings are called f-strings. The f is for format, because Python 
#formats the string by replacing the name of any variable in braces with its 
#value. 

print(f"Hello, {full_name.title()}!")

# Simpler option below
message = f"Hello, {full_name.title()}!"
print(message)
