"""
Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
"""
def round_and_sum(nums):
    # Calculate the length of the list
    n = len(nums)
    
    # Round each number in the list and calculate the sum
    total_sum = sum(map(round, nums))
    
    # Multiply the total sum by the length of the list
    result = total_sum * n
    
    return result

# Test the function with the provided test case
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]) == 243