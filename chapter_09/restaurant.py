class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Stores restaurant name and food type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numberServed = 0

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name} and it serves {self.cuisine_type}")
    
    def open_restaurant(self):
        print('Restaurant is open.')
    def number_served(self):
        print(f"We have served: {self.numberServed} patrons")
    def set_number_served(self, served):
        self.numberServed = served
    def increment_number_served(self, served=1):
        self.numberServed += served

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='Ice Cream', flavors=[]):
        super().__init__(restaurant_name, cuisine_type)
        self.icecreamflavors = flavors

    def available_flavors(self):
        for flavor in self.icecreamflavors:
            print (f"We have {flavor} available")