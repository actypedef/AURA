"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""
def dog_age(human_years):
    # Check if the input age is negative
    if human_years < 0:
        exit()
    # Check if the input age is zero
    elif human_years == 0:
        return 0
    # Check if the input age is one
    elif human_years == 1:
        return 15
    # Check if the input age is two
    elif human_years == 2:
        return 24
    # Calculate dog's age for ages greater than two
    else:
        return 24 + (human_years - 2) * 4

# Test the function with the provided test case
assert dog_age(12) == 61
