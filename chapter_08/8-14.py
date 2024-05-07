def make_car(make, model, **car_info):
    """Build a dictionary containing information about a car"""
    car_info['car_make'] = make
    car_info['car_model'] = model
    return car_info

car_profile = make_car('volvo', 's60',
                       year=2006,
                       color='magic blue',)

print(car_profile)