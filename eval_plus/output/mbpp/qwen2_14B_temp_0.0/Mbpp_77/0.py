"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""
def is_Diff(n):
    # Convert the number to a string to iterate over each digit
    str_n = str(n)
    odd_sum = 0
    even_sum = 0
    
    # Iterate over the digits, summing odd and even positioned digits separately
    for i in range(len(str_n)):
        if i % 2 == 0:
            odd_sum += int(str_n[i])
        else:
            even_sum += int(str_n[i])
    
    # Check if the difference between the sums is divisible by 11
    return (odd_sum - even_sum) % 11 == 0

# Test the function with the provided test case
assert is_Diff(12345) == False
