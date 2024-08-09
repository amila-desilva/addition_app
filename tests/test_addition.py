import pytest
from addition_app.addition import Addition

def test_add_two_numbers():
    adder = Addition()

    assert adder.add_two_numbers(2,3) == 5