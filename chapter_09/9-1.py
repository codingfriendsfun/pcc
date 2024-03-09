class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """The name and cuisine of a restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Indicates the restaurant is open."""
        print(f"{self.restaurant_name} is open for business.")

#Creating an instance of Restaurant()
restaurant = Restaurant('Night Cafe', 'breakfast')

restaurant.describe_restaurant()
restaurant.open_restaurant()