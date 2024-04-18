from city_functions2 import get_city_country

def test_city_country():
    assert 'Long Beach, California, 0' == get_city_country('Long Beach',"California")
def csp():
    assert 'Long Beach, California, 100' == get_city_country('Long Beach',"California", 100)
