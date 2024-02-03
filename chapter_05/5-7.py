# favorite fruits list, with independent ifs

favorite_fruits = ["bananas", "apples", "oranges"]

for fruit in ["bananas", "pears", "apples", "oranges", "kumquats"]:
    if fruit in favorite_fruits:
        print(f"You really like {fruit}!")