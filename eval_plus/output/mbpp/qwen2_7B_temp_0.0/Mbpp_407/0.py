"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""
def rearrange_bigger(n):
    # Convert the number to a list of its digits
    digits = list(str(n))
    
    # Traverse the list from the second last digit to the first digit
    for i in range(len(digits) - 2, -1, -1):
        # If the current digit is smaller than the next digit
        if digits[i] < digits[i + 1]:
            # Find the smallest digit greater than the current digit on the right side
            for j in range(len(digits) - 1, i, -1):
                if digits[j] > digits[i]:
                    # Swap the found digit with the current digit
                    digits[i], digits[j] = digits[j], digits[i]
                    # Sort the digits after the current position to get the smallest possible number
                    digits = digits[:i + 1] + sorted(digits[i + 1:])
                    # Convert the list back to an integer and return it
                    return int(''.join(digits))
    # If no such arrangement exists, return the original number
    return n

# Test the function with the provided test case
assert rearrange_bigger(12) == 21