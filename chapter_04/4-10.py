#chapter_04/4-4.py
numbers = []
for value in range(1, 1000001):
    numbers.append(value)
#4-10
print(f"The first three items in this list are {numbers[0:3]}")
print(f"\nThree items from the middle are {numbers[499998:500001]}")
print(f"\nThe last three items in the list are {numbers[-3:]}")
