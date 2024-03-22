class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Stores restaurant name and food type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name} and it serves {self.cuisine_type}")
    
    def open_restaurant(self):
        print('Restaurant is open.')

restaurant = Restaurant('Hurry Curry', 'Indian Curry')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
    
