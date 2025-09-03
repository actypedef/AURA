"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""
def is_polite(n):
    # Initialize count of polite numbers found
    count = 0
    
    # Start checking from 2 (the first polite number)
    i = 2
    
    # Loop until we find the nth polite number
    while True:
        # Check if the current number is not a power of two
        if ((i & (i - 1)) != 0):
            # Increment the count of polite numbers found
            count += 1
            
            # If we have found the nth polite number, return it
            if count == n:
                return i
        
        # Move to the next number
        i += 1

# Test the function with the provided test case
assert is_polite(7) == 11