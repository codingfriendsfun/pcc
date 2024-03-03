def city_country(name, country):
    """Formats a city, country pair."""
    city_country_formatted = f"{name.title()}, {country.title()}"
    return city_country_formatted

# using city_country() to describe cities
dallas = city_country('dallas', 'america')
london = city_country('london', 'england')
vancouver = city_country('vancouver', 'canada')

#verifies the function and variables are correct
print(dallas)
print(london)
print(vancouver)

