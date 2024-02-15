def make_sandwich(*ingredients):
    print("\nWe received the following order:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('sunflower butter')
make_sandwich('ham', 'cheese', 'mayo')
make_sandwich('roast beef', 'cheese')