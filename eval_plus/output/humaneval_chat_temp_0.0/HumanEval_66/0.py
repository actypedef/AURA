
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
def digitSum(s):
    # Initialize the sum to zero
    total_sum = 0
    
    # Iterate through each character in the string
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Add its ASCII value to the total sum
            total_sum += ord(char)
    
    # Return the computed sum
    return total_sum

# Test cases to verify the correctness of the function
assert digitSum("") == 0
assert digitSum("abAB") == 131
assert digitSum("abcCd") == 67
assert digitSum("helloE") == 69
assert digitSum("woArBld") == 131
assert digitSum("aAaaaXa") == 153