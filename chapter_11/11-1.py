from city_functions import get_city_country

def test_city_country():
    assert 'Long Beach, California' == get_city_country('Long Beach',"California")
