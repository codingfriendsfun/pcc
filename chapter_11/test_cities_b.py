# test suites for 11-1. City, Country
from city_functions_b import city_country

def test_city_country():
    assert "Santiago, Chile" == city_country('santiago', 'chile')

def test_city_country_population():
    assert "Santiago, Chile - population 5000" == city_country('santiago', 'chile', 5000)
