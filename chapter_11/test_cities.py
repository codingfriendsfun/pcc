# test suites for 11-1. City, Country
from city_functions import city_country

def test_city_country():
    assert "Santiago, Chile" == city_country('santiago', 'chile')