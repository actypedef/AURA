"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""
def dog_age(human_years):
    # The first two human years count as 10.5 dog years each
    if human_years <= 2:
        return human_years * 10.5
    else:
        # After the first two human years, each additional year counts as 4 dog years
        return (human_years - 2) * 4 + 21

# Test cases to verify the correctness of the function
assert dog_age(12) == 61
assert dog_age(3) == 27
assert dog_age(0) == 0
assert dog_age(1) == 10.5
assert dog_age(2) == 21