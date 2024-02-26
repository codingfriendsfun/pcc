# 9-1. Restaurant

class Restaurant:
    """ Class model of a restaurant."""

    def __init__(self, name, cuisine):
        """Initialize restaurant"""
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

restaurant = Restaurant("Red Steer", "Sandwiches")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
