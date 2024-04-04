# 10-6. Addition

num1 = input("Enter the first number to be added: ")
num2 = input("Enter the second number to be added: ")

try:
    print(f"The sum is {int(num1) + int(num2)}.")
except ValueError:
    print("Please try again, both your numbers must be in integer format.")