"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""
def wind_chill(v, t):
    # Calculate the wind chill using the formula
    w = 13.12 + 0.6215 * t -  11.37 * v**0.16 + 0.3965 * t * v**0.16
    
    # Round the result to the nearest integer
    return round(w)

# Test the function with the provided test case
assert wind_chill(120, 35) == 40