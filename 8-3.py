# 8-3 T-Shirt

def make_shirt(size, message):
    print(f"Your {size} shirt will say: '{message}'")

make_shirt("large", "This is a positional argument call")
make_shirt(size="medium", message="This is a keyword argument call")