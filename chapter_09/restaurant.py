class Restaurant:
    """A basic model for a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant's name and cuisine."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a description for the information about the restaurant"""
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} food.")

    def open_restaurant(self):
        """Print a statement simulating the restaurant opening."""
        print(f"{self.restaurant_name.title()} is now open!")