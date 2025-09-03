"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""
def dog_age(human_years):
    # Check if the input age is negative
    if human_years < 0:
        exit()
    
    # Calculate the equivalent dog age for the first two years
    elif human_years <= 2:
        dog_years = human_years * 10.5
    
    # Calculate the equivalent dog age for ages beyond two years
    else:
        dog_years = 21 + (human_years - 2) * 4
    
    return dog_years

# Test the function with the provided test case
assert dog_age(12) == 61
