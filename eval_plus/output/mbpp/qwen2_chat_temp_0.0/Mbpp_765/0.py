"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""
def is_polite(n):
    # Initialize count of polite numbers found so far
    count = 0
    
    # Iterate through natural numbers starting from 1
    i = 1
    while True:
        # Check if the current number is not a power of two
        if (i & (i - 1)) != 0:
            # Increment the count of polite numbers
            count += 1
            
            # If we have found n polite numbers, return the current number
            if count == n:
                return i
        
        # Move to the next natural number
        i += 1

# Test the function with the provided test case
assert is_polite(7) == 11
