# 9-4. Restaurant
# based off of 9-1. Restaurant

class Restaurant:
    """ Class model of a restaurant."""

    def __init__(self, name, cuisine, num_served=0):
        """Initialize restaurant"""
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = num_served

    def describe_restaurant(self):
        """Print attributes of the restaurant"""
        print("Restaurant attributes are: ")
        print(f"    Name: {self.restaurant_name}")
        print(f"    Cuisine: {self.cuisine_type}")
        print(f"    Patrons served: {self.cuisine_type}")

    def open_restaurant(self):
        """Print an opening statement"""
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, num_served=0):
        """Reset the number served to a specified value"""
        self.number_served = num_served

    def increment_number_served(self, num_served=1):
        """Increase number served by a provided increment"""
        self.number_served += num_served

# direct assignment
restaurant = Restaurant("Red Steer", "Sandwiches")
print(restaurant.number_served)
restaurant.number_served = 20
print(restaurant.number_served)

# using a method to set a member
restaurant.set_number_served(30)
print(restaurant.number_served)

# using a method to modify a member in a way 
# that is dependent on the existing value 
restaurant.increment_number_served()
print(restaurant.number_served)