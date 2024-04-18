import pytest
from employee import Employee

@pytest.fixture
def new_employee():
    """New employee for test functions."""

    new_employee = Employee('John', 'Doe', 40000)
    return new_employee


def test_give_default_raise(new_employee):
    """Test that the default raise is given."""

    new_employee.give_raise()
    assert new_employee.salary == 45000


def test_give_custom_raise(new_employee):
    """Test that a custom raise is given."""

    new_employee.give_raise(10000)
    assert new_employee.salary == 50000
