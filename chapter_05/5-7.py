fruits = ["orange", "apple", "pineapple", "pear"]
favoriteFruits = ["orange", "pear", "grape"]
for fruit in fruits:
    if fruit.lower() == "orange":
        print("Orange you glad...")
    if fruit.lower() == "pineapple":
        print("think of the pizza")
    if fruit.lower() in favoriteFruits:
        print(f"You really like " + fruit + "s!")
