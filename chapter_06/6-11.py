# using dictionaries to store info about cities

cities = {
    'FakeCity1' : {
        'name' : 'FakeCity1',
        'country' : 'FakeCountry1',
        'pop' : 10000000
    },
    'FakeCity2' : {
        'name' : 'FakeCity2',
        'country' : 'FakeCountry2',
        'pop' : 8000
    },  
    'FakeCity3' : {
        'name' : 'FakeCity3',
        'country' : 'FakeCountry3',
        'pop' : 70000
    }
}


for city, info in cities.items():
    print(city)
    for key in info:
        print(f"{key} : {info[key]}")