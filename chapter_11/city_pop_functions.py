
def get_formatted_location(city, country, population=''):
    """Generate a neatly formatted location"""
    if population:
        city_country = f"{city.title()}, {country.title()} "
        city_country += f"has a population of: {population}"

    else:
        city_country = f"{city.title()}, {country.title()}"

    return city_country
