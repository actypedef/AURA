"""
Write a function that takes in two numbers and returns a tuple with the second number and then the first number.
assert swap_numbers(10,20)==(20,10)
"""
def swap_numbers(x, y):
    # Create a tuple with the elements swapped
    return (y, x)

# Test the function with the provided test case
assert swap_numbers(10, 20) == (20, 10)
