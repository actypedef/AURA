"""
Write a function to find the directrix of a parabola.
assert parabola_directrix(5,3,2)==-198
"""
def parabola_directrix(a, b, c):
    # Calculate the directrix using the formula: y = (c - ((b**2) + 1)) / (4 * a)
    return int(c - ((b ** 2) + 1) / (4 * a))

# Test the function with the provided test case
assert parabola_directrix(5, 3, 2) == -198
