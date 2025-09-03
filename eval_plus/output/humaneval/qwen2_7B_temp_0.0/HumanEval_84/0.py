
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
def solve(N):
    # Convert the integer to a string to iterate over each digit
    digit_sum = sum(int(digit) for digit in str(N))
    # Convert the sum of digits to binary and remove the '0b' prefix
    return bin(digit_sum)[2:]

# Test cases
assert solve(1000) == "1"
assert solve(150) == "110"
assert solve(147) == "1100"

# Explanation:
# The function `solve` takes an integer `N` as input.
# It calculates the sum of the digits of `N` using a generator expression inside the `sum` function.
# The result is then converted to a binary string using the `bin` function, which returns a string starting with '0b'.
# To get the actual binary representation without the '0b' prefix, we slice the string from the second character onwards.
# Finally, the function returns this binary string.