# 9-6. Ice Cream Stand
# based off of 9-4

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

class IceCreamStand(Restaurant):
    """Subclass of Restaurant specific to ice cream"""

    def __init__(self, name, flavors=[], num_served=0):
        super().__init__(name, "Ice Cream", num_served)
        self.flavors = flavors

    def list_flavors(self):
        print(f"{self.restaurant_name} serves the following flavors: ")
        for flavor in self.flavors:
            print(f"    {flavor}")

myStand = IceCreamStand("Iceeeey", ["Vanilla", "Chocolate", "Strawberry"])

myStand.list_flavors()
