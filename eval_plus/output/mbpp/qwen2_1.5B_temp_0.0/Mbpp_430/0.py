"""
Write a function to find the directrix of a parabola.
assert parabola_directrix(5,3,2)==-198
"""
def parabola_directrix(a, b, c):
    # Calculate the discriminant
    D = (4*a*c) - (b**2)
    
    # Check if the discriminant is positive
    if D > 0:
        # If positive, calculate the directrix using the formula: y = -(4ac + b^2) / (4a)
        return -(4*a*c + b**2) / (4*a)
    else:
        # If not positive, the parabola does not have a directrix
        return None

# Test cases
assert parabola_directrix(5,3,2)==-198