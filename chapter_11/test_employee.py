# test suite for 11-3. Employee
# test_employee.py

from employee import Employee
import pytest


@pytest.fixture
def employee():
    """employee to be shared by all tests"""
    return Employee("Huckleberry", "Finn", 0)


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 5000


def test_give_custom_raise(employee):
    employee.give_raise(10)
    assert employee.salary == 10
