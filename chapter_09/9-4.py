class Restaurant:
    """A basic model for a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant's name and cuisine."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print a description for the information about the restaurant"""
        print(
            f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} food."
        )

    def open_restaurant(self):
        """Print a statement simulating the restaurant opening."""
        print(f"{self.restaurant_name.title()} is now open!")

    def patrons_served(self):
        """Print a statement for the number of patrons the restaurant has served."""
        print(f"We have now served {self.number_served} patrons today.")

    def set_number_served(self, patrons):
        """Set the number of patrons served to a specific value.

        :param patrons: 

        """
        self.number_served = patrons

    def increment_number_served(self, people):
        """Add the given number of people to patrons served.

        :param people: 

        """
        self.number_served += people


restaurant = Restaurant("lucia's tavola", "italian")

print(
    f"One of my favorite restaurants was an {restaurant.cuisine_type.title()}"
    f" restaurant named {restaurant.restaurant_name.title()}."
)

# Print statements detailing the restaurant info and opening the restaurant.
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Prove that the number of patrons served is set to zero.
restaurant.patrons_served()

# Set the number of patrons served to a specific number and print the statement.
restaurant.number_served = 7
restaurant.patrons_served()

# Use the set_number_served() method to adjust the number served.
restaurant.set_number_served(9)
restaurant.patrons_served()

# Use the increment_number_served() method to adjust the number served.
restaurant.increment_number_served(11)
restaurant.patrons_served()
