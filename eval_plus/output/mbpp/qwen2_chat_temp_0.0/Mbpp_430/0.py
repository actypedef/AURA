"""
Write a function to find the directrix of a parabola.
assert parabola_directrix(5,3,2)==-198
"""
def parabola_directrix(a, b, c):
    # Calculate the directrix using the formula: -b^2 + 4ac
    return -b**2 + 4*a*c

# Test the function with the provided test case
assert parabola_directrix(5, 3, 2) == -198