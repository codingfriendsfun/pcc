# creating a function that accepts a city and a country and returns the pair
# seperated by a comma and spce
def city_country(city="Long Beach", country="United States"):
    """

    :param city:  (Default value = "Long Beach")
    :param country:  (Default value = "United States")

    """
    paired = f"{city}, {country}"
    return paired.title()


LongBeach = city_country()
LosAngeles = city_country("Los Angeles")
Paris = city_country("paris", "france")

print(LongBeach)
print(Paris)
print(LosAngeles)
