
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    else:
        return 2 * (10 ** (n - 1)) - 10 ** (n - 2)

def test_starts_one_ends():
    assert starts_one_ends(1) == 1
    assert starts_one_ends(2) == 18
    assert starts_one_ends(3) == 180
    assert starts_one_ends(4) == 1800
    assert starts_one_ends(5) == 18000
    assert starts_one_ends(6) == 180000
    assert starts_one_ends(7) == 1800000
    assert starts_one_ends(8) == 18000000
    assert starts_one_ends(9) == 180000000
    assert starts_one_ends(10) == 1800000000
    assert starts_one_ends(11) == 18000000000
    assert starts_one_ends(12) == 180000000000
    assert starts_one_ends(13) == 1800000000000
    assert starts_one_ends(14) == 18000000000000
    assert starts_one_ends(15) == 180000000000000
    assert starts_one_ends(16) == 1800000000000000
    assert starts_one_ends(17) == 18000000000000000
    assert starts_one_ends(18) == 180000000000000000
    assert starts_one_ends(19) == 1800000000000000000
    assert starts_one_ends(20) == 18000000000000000000
    assert starts_one_ends(21) == 180000000000000000000
    assert starts_one_ends(22) == 1800000000000000000000
    assert starts_one_ends(23) == 18000000000000000000000
    assert starts_one_ends(24) == 180000000000000000000000
    assert starts_one_ends(25) == 1800000000000000000000000
    assert starts_one_ends(26) == 18000000000000000000000000
    assert starts_one_ends(27) == 180000000000000000