
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a
    return [i for i in range(a, b + 1) if i % 2 == 0]


def test_generate_integers():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(1, 10) == [2, 4, 6, 8, 10]
    assert generate_integers(10, 1) == [2, 4, 6, 8, 10]
    assert generate_integers(1, 1) == []
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 1) == [2]
    assert generate_integers(1, 3) == [2]
    assert generate_integers(3, 1) == [2]
    assert generate_integers(1, 4) == [2, 4]
    assert generate_integers(4, 1) == [2, 4]
    assert generate_integers(1, 5) == [2, 4]
    assert generate_integers(5, 1) == [2, 4]
    assert generate_integers(1, 6) == [2, 4, 6]
    assert generate_integers(6, 1) == [2, 4, 6]
    assert generate_integers(1, 7) == [2, 4, 6]
    assert generate_integers(7, 1) == [2, 4, 6]
    assert generate_integers(1, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 1) == [2, 4, 6, 8]
    assert generate_integers(1, 9) == [2, 4, 6, 8]
    assert generate_integers(9, 1) == [2, 4, 6, 8]
    assert generate_integers(1, 10) == [2, 4, 6, 8, 10]
    assert generate_integers(10, 1) == [2, 4, 6, 8, 10]
    assert generate_integers(1, 11) == [2, 4, 6, 8, 10]
    assert generate_integers(11, 1) == [2, 4, 6, 8, 10]
    assert generate_integers(1, 12) == [2, 4, 6, 8, 10, 12]
    assert generate_integers(12, 1) == [2, 4, 6, 8, 10