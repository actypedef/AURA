"""
Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
"""
def round_and_sum(numbers):
    # Round each number in the list and store the rounded numbers in a new list
    rounded_numbers = [round(num) for num in numbers]
    
    # Calculate the sum of the rounded numbers
    total_sum = sum(rounded_numbers)
    
    # Multiply the sum by the length of the list
    result = total_sum * len(numbers)
    
    return result

# Test the function with the provided test case
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]) == 243
