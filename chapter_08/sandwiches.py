#function from 8-12.py 

def sandwich_toppings(*toppings):
    """Lists the toppings added to a sandwich."""
    print("\nAdding the following toppings to your sandwich:")
    for topping in toppings:
        print(f"- {topping}")
