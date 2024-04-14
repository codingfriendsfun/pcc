# 11-2. Population

def city_country(city, country, pop=0):
    if pop == 0:
        return f"{city.title()}, {country.title()}"
    return f"{city.title()}, {country.title()} - population {pop}"
