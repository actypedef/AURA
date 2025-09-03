"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""
def reverse_vowels(s):
    # Define vowels
    vowels = 'aeiouAEIOU'
    
    # Convert the string to a list for easier manipulation
    s = list(s)
    
    # Initialize pointers for the start and end of the string
    i, j = 0, len(s) - 1
    
    # Loop until the two pointers meet
    while i < j:
        # Move the left pointer if the current character is not a vowel
        if s[i] not in vowels:
            i += 1
        # Move the right pointer if the current character is not a vowel
        elif s[j] not in vowels:
            j -= 1
        # Swap the vowels if both pointers are at vowels
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    
    # Join the list back into a string and return it
    return ''.join(s)

# Test the function with the provided test case
assert reverse_vowels("Python") == "Python"
