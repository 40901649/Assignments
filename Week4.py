# Week 4 - 19/05
import pylint
# 1. Write a python program to understand lambda function.
def function_name(val2):
    return lambda val1: val1*val2


my_result = function_name(20)
print(my_result)
print(my_result(10))

# 2. Write a python program to understand pytest.
import pytest


def add_two(a,b):
    return a+b


def test_method():
    assert add_two(10,20) == 30
    assert add_two(5,5) == 10    # AssertionError
    assert add_two(15,2) == 17 # TypeError: add_two() takes 2 positional arguments but 3 were given

test_method()