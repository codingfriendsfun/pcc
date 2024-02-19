# 8-14. Cars

def make_car(make, model, **features):
    # I didn't like that the book example didn't start with name info
    # so I fixed it

    car_info = {}
    car_info["make"] = make
    car_info["model"] = model

    return {**car_info, **features}

print(make_car('subaru', 'outback', color='blue', tow_package=True))