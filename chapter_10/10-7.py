from pathlib import Path

def count_numbers():
    """
    Sum two numbers.
    """
    while True:

        print("(Enter 'q' at any time to quit)")

        num1 = input("Enter your first number: ")

        if num1 == 'q':
            return False

        num2 = input("Enter your second number: ")

        if num2 == 'q':
            return False

        try:
            sum = int(num1) + int(num2)
        
        except ValueError:
            print("Please enter only integers.")
        
        else:
            print(sum)
    
    
count_numbers()
