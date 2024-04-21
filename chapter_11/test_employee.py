from employee import Employee

def test_first_and_last():
    Ravi = Employee('Ravi',"Ghotra", 38000)
    assert 'Ravi Ghotra' == f'{Ravi.first} {Ravi.last}'
    assert 38000 == Ravi.salary
def test_give_raise():
    Ravi = Employee('Ravi',"Ghotra", 38000)
    Ravi.give_raise()
    assert 'Ravi Ghotra' == f'{Ravi.first} {Ravi.last}'
    assert 43000 == Ravi.salary
