def store_car_info(manufacturer, model, **features):
    """Stores information about a car in a dictionary.

    :param manufacturer: The car's manufacturer.
    :type manufacturer: str
    :param model: The car's model name.
    :type model: str
    :param **features: Arbitrary keyword arguments (e.g., color, other features).
    :returns: A dictionary containing car information.
    :rtype: dict

    """
    features["Manufacturer"] = manufacturer
    features["Model"] = model
    return features


# Example usage
my_car = store_car_info(
    manufacturer="Chevy",
    model="Volt",
    color="Blue",
    Sound="Bose Stereo",
    Navigation=True,
)

# Print the stored car information
print("Car Information:")
for key, value in my_car.items():
    print(f"{key}: {value}")
