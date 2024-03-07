# model and manufacturer are required
def car_details(model, manufacturer, **car_info):
    """Build a dictionary containing details about a car

    :param model:
    :param manufacturer:
    :param **car_info:

    """
    car_info["model"] = model
    car_info["manufacturer"] = manufacturer
    return car_info


# creating 2 cars using the function
car_1 = car_details("miata", "mazda", convertible=True, color="white")
car_2 = car_details("accord", "honda", color="blue", luxury_trim=True)

# verifies the function worked to store all key-value pairs
print(car_1)
print(car_2)
