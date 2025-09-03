"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""
def dog_age(human_years):
    # Check if the input human years are negative
    if human_years < 0:
        exit()
    # Calculate the first two years of a dog's life
    elif human_years <= 2:
        dog_years = human_years * 10.5
    # Calculate the additional years after the first two years
    else:
        dog_years = 21 + (human_years - 2) * 4
    return dog_years

# Test the function with the provided test case
assert dog_age(12) == 61
