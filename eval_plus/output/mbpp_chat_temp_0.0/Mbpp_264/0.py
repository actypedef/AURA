"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""
def dog_age(human_years):
    # Check if the input age is negative
    if human_years < 0:
        exit()
    # For the first two years, a dog year is equal to 10.5 human years
    elif human_years <= 2:
        dog_years = human_years * 10.5
    # After two years, each dog year is equal to 4 human years
    else:
        dog_years = 21 + (human_years - 2) * 4
    return dog_years

# Test the function with the provided test case
assert dog_age(12) == 61
