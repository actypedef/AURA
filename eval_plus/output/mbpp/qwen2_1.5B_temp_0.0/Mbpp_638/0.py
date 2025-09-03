"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""
def wind_chill(wind_velocity, temperature):
    # Calculate the wind chill index using the formula
    wind_chill_index = 13.12 + 0.6215 * temperature - 11.32 * (wind_velocity ** 0.16) + 0.3965 * temperature * (wind_velocity ** 0.16) - 0.8664 * (temperature ** 0.16) * (wind_velocity ** 0.16)
    # Round the result to the nearest integer
    return round(wind_chill_index)

# Test cases to verify the correctness of the function
assert wind_chill(120,35)==40
assert wind_chill(70,20)==16
assert wind_chill(50,-10)==-1
assert wind_chill(100,0)==0
assert wind_chill(20,100)==-10