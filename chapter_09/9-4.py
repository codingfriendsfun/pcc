class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """The name and cuisine of a restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Indicates the restaurant is open."""
        print(f"{self.restaurant_name} is open for business.")
    
    def customers_served(self):
        """The number of customers a restaurant has served."""
        print(f"This restaurant has served {self.number_served} customers.")

    def update_customers_served(self, new_guests):
        """Updates the number of customers served at a restuarant."""
        self.number_served += new_guests


#Creating an instance of Restaurant()
restaurant = Restaurant('Night Cafe', 'breakfast')

#Updating customers served from 0 to 5
restaurant.customers_served()
restaurant.update_customers_served(5)
restaurant.customers_served()