from city_functions import get_city_country

def test_city_country():
    """Do places like 'Edinburgh, Scotland' work?"""
    formatted_city = get_city_country('edinburgh', 'scotland')
    assert formatted_city == "Edinburgh, Scotland"