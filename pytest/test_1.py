import pytest

def a(a,b):
    return a+b

def test_a():
    assert a(3,4) == 7
