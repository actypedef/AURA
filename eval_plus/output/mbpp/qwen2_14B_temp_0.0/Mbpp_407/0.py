"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""
import sys

def rearrange_bigger(num):
    # Convert the number to a list of its digits
    digits = list(str(num))
    
    # Traverse the list from right to left to find the first digit that is smaller than the digit next to it
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    # If no such digit is found, return -1 as no rearrangement can make a bigger number
    if i == -1:
        return -1
    
    # Find the smallest digit on the right side of the found digit that is larger than the found digit
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    # Swap the found digit with the smallest larger digit
    digits[i], digits[j] = digits[j], digits[i]
    
    # Reverse the sequence of digits to the right of the original position of the found digit
    digits = digits[:i + 1] + digits[i + 1:][::-1]
    
    # Convert the list of digits back to an integer and return it
    return int(''.join(digits))

# Test the function with the provided test case
assert rearrange_bigger(12) == 21
