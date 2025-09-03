"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""
def reverse_vowels(s):
    # Convert the string to a list for mutable operations
    s = list(s)
    
    # Initialize pointers for the start and end of the string
    i, j = 0, len(s) - 1
    
    # Define a set of vowels for easy checking
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Loop until the two pointers meet or cross each other
    while i < j:
        # Move the left pointer if it's not pointing at a vowel
        if s[i] not in vowels:
            i += 1
        # Move the right pointer if it's not pointing at a vowel
        elif s[j] not in vowels:
            j -= 1
        else:
            # Swap the vowels found at both pointers
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    
    # Join the list back into a string and return it
    return ''.join(s)

# Test the function with the provided test case
assert reverse_vowels("Python") == "Python"