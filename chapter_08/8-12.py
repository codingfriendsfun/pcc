#items on a sandwich
def sandwich_toppings(*toppings):
    """Lists the toppings added to a sandwich."""
    print("\nAdding the following toppings to your sandwich:")
    for topping in toppings:
        print(f"- {topping}")

#different sandwiches
sandwich_toppings('cheese', 'ham')
sandwich_toppings('olives', 'peppers', 'turkey', 'mayo')
sandwich_toppings('peanut butter')