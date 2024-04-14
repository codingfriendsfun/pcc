import pytest
from employee import Employee

# Original work without fixture
#def test_give_default_raise():
#    """Test giving the employee the default raise"""
#    nriley = Employee('noelle', 'riley', 60000)
#    nriley.give_raise()
#    assert nriley.salary == 65000

#def test_give_custom_raise():
#    """Test giving the employee a custom raise"""
#    nriley = Employee('noelle', 'riley', 60000)
#    nriley.give_raise(100000)
#    assert nriley.salary == 160000

# With fixture
@pytest.fixture
def nriley():
    """An employee for testing"""
    nriley = Employee('noelle', 'riley', 60000)
    return nriley

def test_give_default_raise(nriley):
    """Test giving the employee the default raise"""
    nriley.give_raise()
    assert nriley.salary == 65000

def test_give_custom_raise(nriley):
    """Test giving the employee a custom raise"""
    nriley.give_raise(100000)
    assert nriley.salary == 160000