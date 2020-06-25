import pytest
import requests

def a(x):
    return x+1

def test_a():
    assert a(3) == 5

# 括号内ctrl+ p 可以查看传参
requests.post()