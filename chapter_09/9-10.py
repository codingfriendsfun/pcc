from restaurant import IceCreamStand as ICS
from restaurant import Restaurant as Res


Spacekinflavors = ["Chocolate", "Vanilla", "Strawberry", "Berts Every flavor", "Poop"]
SpacekinRobins = ICS("Spacekin Robins", "Astronaut Ice Cream", Spacekinflavors)
my_rr = Res('Hurry Curry', 'Indian Curry')

SpacekinRobins.available_flavors()
my_rr.describe_restaurant()
