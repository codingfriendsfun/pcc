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

class IceCreamStand(Restaurant):
    """A model for an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type, flavor0, flavor1, flavor2):
        """
        Initialize attritubes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavor0 = flavor0
        self.flavor1 = flavor1
        self.flavor2 = flavor2

    def list_flavors(self):
        """Print a statement describing the flavors offered by the ice cream stand."""
        flavors = (self.flavor0, self.flavor1, self.flavor2)
        print(f"{self.restaurant_name.title()} offers the following flavors:")
        for flavor in flavors:
            print(flavor)

monument_icecream = IceCreamStand(
    'monument ice cream', 
    'ice cream', 
    'chocolate',
    'vanilla',
    'butter crunch'
    )

monument_icecream.list_flavors()