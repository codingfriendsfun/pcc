def describe_city(name, country='america'):
    """Describes a city and country pair."""
    print(f"{name.title()} is in {country.title()}.")

describe_city('dallas')
describe_city('houston')
describe_city('vancouver', 'canada')