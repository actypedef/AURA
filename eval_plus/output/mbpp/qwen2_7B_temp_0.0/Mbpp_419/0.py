"""
Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
"""
def round_and_sum(nums):
    # Round each number in the list using map and lambda functions
    rounded_nums = list(map(lambda x: round(x), nums))
    
    # Calculate the sum of the rounded numbers
    total_sum = sum(rounded_nums)
    
    # Multiply the total sum by the length of the list
    result = total_sum * len(nums)
    
    return result

# Test the function with the provided test case
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]) == 243