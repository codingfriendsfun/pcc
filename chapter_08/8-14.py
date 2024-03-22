def store_car_info(manufacturer, model, **features):
    """
    Stores information about a car in a dictionary.

    Args:
        manufacturer (str): The car's manufacturer.
        model (str): The car's model name.
        **features: Arbitrary keyword arguments (e.g., color, other features).

    Returns:
        dict: A dictionary containing car information.
    """
    features["manufacturer"] = manufacturer
    features["model"] = model
    return features


# Example usage
my_car = store_car_info(
    manufacturer="Chevy",
    model="Volt",
    color="Blue",
    Bonus=["Bose Stereo", "Navigation"],
)

# Print the stored car information
print("Car Information:")
for key, value in my_car.items():
    print(f"{key}: {value}")
