"""
Write a function that takes in two numbers and returns a tuple with the second number and then the first number.
assert swap_numbers(10,20)==(20,10)
"""
def swap_numbers(num1, num2):
    # Return a tuple with the second number followed by the first number
    return (num2, num1)

# Test the function with the provided test case
assert swap_numbers(10, 20) == (20, 10)
