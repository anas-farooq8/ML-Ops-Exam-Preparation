from app import add

def test_add():
    a = 5
    b = 6

    actual_result = add(a, b)
    expected_result = 11
    print(actual_result)
    assert actual_result == expected_result

test_add()