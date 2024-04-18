from city_functions import get_city_country

def test_city_country():
    LB = get_city_country('Long Beach',"California")
    assert LB == 'Long Beach, California'
