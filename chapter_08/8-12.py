#items on a sandwich
def sandwich_toppings(*toppings):
    print("\nAdding the following toppings to your sandwich:")
    for topping in toppings:
        print(f"- {topping}")

#different sandwiches
sandwich_toppings('cheese', 'ham')
sandwich_toppings('olives', 'peppers', 'turkey', 'mayo')
sandwich_toppings('peanut butter')