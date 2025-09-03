"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""
def reverse_vowels(s):
    # Define a set of vowels for quick lookup
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    # Convert the string into a list of characters
    s_list = list(s)
    
    # Initialize two pointers: one at the start and one at the end of the list
    left, right = 0, len(s) - 1
    
    # Loop until the two pointers meet or cross each other
    while left < right:
        # Move the left pointer to the right if it points to a non-vowel
        while left < right and s_list[left] not in vowels:
            left += 1
        
        # Move the right pointer to the left if it points to a non-vowel
        while left < right and s_list[right] not in vowels:
            right -= 1
        
        # Swap the vowels at the current positions
        s_list[left], s_list[right] = s_list[right], s_list[left]
        
        # Move both pointers towards the center
        left += 1
        right -= 1
    
    # Join the list back into a string and return it
    return ''.join(s_list)

# Test cases to verify the correctness of the solution
assert reverse_vowels("Python") == "Python"
assert reverse_vowels("Hello World!") == "Holle Wdlor!"
assert reverse_vowels("Programming") == "Prigrammong"
assert reverse_vowels("") == ""
assert reverse_vowels("AEIOUaeiou") == "uoieAEOU"