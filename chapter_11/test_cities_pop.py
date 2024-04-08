from city_pop_functions import get_formatted_location

def test_city_country_population():
    """Verify locations are formatted correctly with populations."""
    formatted_location = get_formatted_location(
        'santiago', 'chile', population=5000000)
    assert formatted_location == 'Santiago, Chile has a population of: 5000000'
