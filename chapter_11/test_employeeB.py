import pytest
from employee import Employee

@pytest.fixture
def hire():
    """Create an new Employee from input for the tests"""
    return Employee('Ravi', 'Ghotra', 0)

def test_first_and_last(hire):
    assert "Ravi Ghotra" == f'{hire.first} {hire.last}'
    assert hire.salary == 0
def test_give_raise(hire):
    hire.give_raise()
    assert hire.salary == 5000
