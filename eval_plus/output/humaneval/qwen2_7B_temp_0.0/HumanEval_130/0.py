
def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
def tri(n):
    # Initialize the Tribonacci sequence with the first three values
    tribonacci = [1, 3, 2]
    
    # If n is less than 3, return the slice of the sequence up to n+1
    if n < 3:
        return tribonacci[:n+1]
    
    # Calculate the rest of the sequence up to n+1
    for i in range(3, n+1):
        if i % 2 == 0:
            tribonacci.append(1 + i / 2)
        else:
            tribonacci.append(tribonacci[i-1] + tribonacci[i-2] + tribonacci[i+1])
    
    return tribonacci

# Test cases