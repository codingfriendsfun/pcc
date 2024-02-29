# for exercise 9-10

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
        print(f"    Patrons served: {self.number_served}")

    def open_restaurant(self):
        """Print an opening statement"""
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, num_served=0):
        """Reset the number served to a specified value"""
        self.number_served = num_served

    def increment_number_served(self, num_served=1):
        """Increase number served by a provided increment"""
        self.number_served += num_served
