"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""
def rearrange_bigger(n):
    # Convert the number to a list of its digits
    digits = [int(digit) for digit in str(n)]
    
    # Find the first digit from the right that is smaller than the digit immediately before it
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    # If no such digit is found, return -1 (no bigger number can be formed)
    if i == -1:
        return -1
    
    # Find the smallest digit on the right side of 'i' that is greater than digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    # Swap digits at positions 'i' and 'j'
    digits[i], digits[j] = digits[j], digits[i]
    
    # Sort the digits after position 'i' to get the smallest possible number
    digits[i + 1:] = sorted(digits[i + 1:])
    
    # Convert the list of digits back to an integer
    return int(''.join(map(str, digits)))

# Test cases
assert rearrange_bigger(12) == 21
assert rearrange_bigger(53) == 56
assert rearrange_bigger(987654321) == 987654321
assert rearrange_bigger(111) == -1