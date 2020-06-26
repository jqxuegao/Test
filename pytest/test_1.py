import pytest

def add(a,b):
    return a+b

# pytest -vv -m g1
# 仅执行g1分组
# --html = report.html （pip pytest-html）
# pytest.mark.parametrize:利用pytest参数化抛弃ddt
@pytest.mark.g1
@pytest.mark.parametrize(
    'a,b,expected',
    [
        (1,1,2),
        (2,2,4),
        (10,2,12),
    ]
)
def test_add(a,b,expected):
    assert add(a,b) == expected