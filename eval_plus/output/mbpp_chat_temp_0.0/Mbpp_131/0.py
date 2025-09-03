"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""
def reverse_vowels(s):
    # Define a set of vowels for quick lookup
    vowels = 'aeiouAEIOU'
    
    # Convert the string into a list for mutable operations
    s_list = list(s)
    
    # Initialize two pointers, one at the start and one at the end of the string
    left, right = 0, len(s) - 1
    
    # Loop until the two pointers meet or cross each other
    while left < right:
        # Move the left pointer to the right until it points to a vowel
        if s[left] not in vowels:
            left += 1
        # Move the right pointer to the left until it points to a vowel
        elif s[right] not in vowels:
            right -= 1
        else:
            # Swap the vowels found by the left and right pointers
            s_list[left], s_list[right] = s_list[right], s_list[left]
            # Move both pointers towards the center
            left += 1
            right -= 1
    
    # Join the list back into a string and return it
    return ''.join(s_list)

# Test the function with the provided test case
assert reverse_vowels("Python") == "Python"