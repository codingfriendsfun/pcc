def get_city_country(city_name, country_name, population=''):
    """Generated a formatted city and country with population mandatory"""
    formatted_city = f"{city_name.title()}, {country_name.title()}"
    if population:
        city_data = f"{formatted_city} - population {population}"
        return city_data
    else:
        return formatted_city