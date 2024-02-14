num = input("Give me a number and I will say if it's a multiple of 10! ")
num= int(num)

if num % 10 == 0:
    print(f"\n{num} is a multiple of 10!")
else:
    print(f"\n{num} is not a multiple of 10!")