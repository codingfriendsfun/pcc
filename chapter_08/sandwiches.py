#function from 8-12.py 

def sandwich_toppings(*toppings):
    print("\nAdding the following toppings to your sandwich:")
    for topping in toppings:
        print(f"- {topping}")
