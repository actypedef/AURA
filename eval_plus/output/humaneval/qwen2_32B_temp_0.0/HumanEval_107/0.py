
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return even_count, odd_count


def test_even_odd_palindrome():
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(12) == (4, 6)
    assert even_odd_palindrome(100) == (9, 45)
    assert even_odd_palindrome(1000) == (99, 450)
    assert even_odd_palindrome(10000) == (999, 4500)
    assert even_odd_palindrome(100000) == (9999, 45000)
    assert even_odd_palindrome(1000000) == (99999, 450000)
    assert even_odd_palindrome(10000000) == (999999, 4500000)
    assert even_odd_palindrome(100000000) == (9999999, 45000000)
    assert even_odd_palindrome(1000000000) == (99999999, 450000000)
    assert even_odd_palindrome(10000000000) == (999999999, 4500000000)
    assert even_odd_palindrome(100000000000) == (9999999999, 45000000000)
    assert even_odd_palindrome(1000000000000) == (99999999999, 450000000000)
    assert even_odd_palindrome(10000000000000) == (999999999999, 4500000000000)
    assert even_odd_palindrome(1000000000000