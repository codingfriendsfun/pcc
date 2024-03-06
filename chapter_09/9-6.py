class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """The name and cuisine of a restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Indicates the restaurant is open."""
        print(f"{self.restaurant_name} is open for business.")

class IceCreamStand(Restaurant):
    """Flavors of an ice cream stand."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the parent attributes and the class attributes."""

        super().__init__(restaurant_name, cuisine_type)
        

    def store_flavors(self, flavors):
        """Creates an inventory of flavors served."""

        self.flavors = flavors

    def list_flavors(self):
        """List the flavors available."""
        
        print("We serve the following flavors: ")
        for flavor in self.flavors:
            print(flavor.title())
        
          
my_stand = IceCreamStand('frozone', 'ice cream')

my_stand.store_flavors(['vanilla', 'java', 'mint chocolate chip', 'pistachio'])
my_stand.list_flavors()

