"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""
def newman_prime(n):
    # Initialize variables for the Newman-Shanks-Williams sequence
    x = 1
    y = 2
    z = 0
    
    # Loop until we have found n primes
    while True:
        # Calculate the next term in the sequence
        z = (x + y * y - 1) % (2 * y)
        
        # Check if the current term is prime
        if z > 1:
            # If it's not prime, update x and y for the next iteration
            x = y
            y = z
        else:
            # If it's prime, decrement n and check if we've reached the desired prime count
            n -= 1
            if n == 0:
                return y

# Test the function with the provided test case
assert newman_prime(3) == 7