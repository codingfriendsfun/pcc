# 10 conditional tests

integer = 6
print("The integer 6 should be less than ten.")
print(integer < 10)
# true 1

print("The integer 6 should be greater than 5.")
print(integer > 5)
# true 2

print("The string 'six' is not equal to 6.")
print('six' == 6)
# false 1

print("The integer 6 is the same as the value 6.")
print(integer == 6)
# true 3

print("Upper case 'L' is not the same as lower case 'l'.")
print('L' == 'l')
# false 2

print("3 is within range(1,5).")
print(3 in range(1,5))
# true 4

print("5 is not within range(1,5).")
print(5 in range(1,5))
# false 3

name = "Alexa"
print("My name is Alexa.")
print(name == "Alexa")
# true 5

name = "notAlexa"
print("Your name is probably not Alexa.")
print(name == "Alexa")
# false 4

print("True is not less than false")
print("False" > "True")
# false 5


