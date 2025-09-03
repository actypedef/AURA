"""
Write a function to find the directrix of a parabola.
assert parabola_directrix(5,3,2)==-198
"""
def parabola_directrix(a, b, c):
    # Calculate the directrix using the formula for a parabola
    directrix = (int)(c - ((b * b) + 1) / (4 * a))
    return directrix

# Test the function with the provided test case
assert parabola_directrix(5, 3, 2) == -198
