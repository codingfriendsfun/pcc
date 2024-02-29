def city_country(name, country):
    city_country_formatted = f"{name.title()}, {country.title()}"
    return city_country_formatted

dallas = city_country('dallas', 'america')
london = city_country('london', 'england')
vancouver = city_country('vancouver', 'canada')
print(dallas)
print(london)
print(vancouver)

