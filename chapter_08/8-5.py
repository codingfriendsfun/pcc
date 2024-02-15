def describe_city(city_name, country='united states'):
    print(f"{city_name.title()} is in {country.title()}")

describe_city('boston')
describe_city('edinburgh', 'scotland')
describe_city('san diego')