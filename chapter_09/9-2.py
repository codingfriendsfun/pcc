class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Stores restaurant name and food type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name} and it serves {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f'{self.restaurant_name} is open.')

restaurant = Restaurant('Hurry Curry', 'Indian Curry')
restaurant.describe_restaurant()
restaurant.open_restaurant()
    
restaurant2 = Restaurant('Mario Mammys', 'Italian')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant('The Salad Bar', 'The green sheet')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()