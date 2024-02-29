def describe_city(name, country='america'):
    print(f"{name.title()} is in {country.title()}.")

describe_city('dallas')
describe_city('houston')
describe_city('vancouver', 'canada')