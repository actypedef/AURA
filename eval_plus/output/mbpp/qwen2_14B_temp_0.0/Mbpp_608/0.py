"""
Write a python function to find nth bell number.
assert bell_Number(2) == 2
"""
def bell_Number(n):
    # Initialize a list to store Bell numbers
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    
    # Fill the Bell triangle
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    
    # Return the nth Bell number
    return bell[n][0]

# Test the function with the provided test case
assert bell_Number(2) == 2