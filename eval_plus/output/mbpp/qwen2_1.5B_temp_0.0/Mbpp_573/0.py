"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""
def unique_product(numbers):
    # Create an empty set to store unique numbers
    unique_numbers = set()
    
    # Iterate through each number in the input list
    for num in numbers:
        # Add the number to the set if it's not already present
        unique_numbers.add(num)
    
    # Calculate the product of all unique numbers using the reduce function from functools module
    import functools
    return functools.reduce(lambda x, y: x * y, unique_numbers)

# Test the function with the provided test case
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000