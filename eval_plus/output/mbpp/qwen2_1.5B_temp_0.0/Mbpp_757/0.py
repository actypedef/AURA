"""
Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""
def count_reverse_pairs(str_list):
    # Create an empty dictionary to store the frequency of each string
    str_freq = {}
    
    # Iterate over each string in the list
    for s in str_list:
        # Reverse the string
        reversed_s = s[::-1]
        
        # If the reversed string exists in the dictionary, increment its count
        if reversed_s in str_freq:
            str_freq[reversed_s] += 1
        else:
            # Otherwise, add the reversed string to the dictionary with a count of 1
            str_freq[reversed_s] = 1
    
    # Initialize a counter for the number of reverse pairs
    reverse_pairs_count = 0
    
    # Iterate over each string in the list again
    for s in str_list:
        # Reverse the string
        reversed_s = s[::-1]
        
        # Check if the reversed string exists in the dictionary and has a count greater than 1
        if reversed_s in str_freq and str_freq[reversed_s] > 1:
            # Add the count of the reversed string to the total count of reverse pairs
            reverse_pairs_count += str_freq[reversed_s] - 1
    
    return reverse_pairs_count

# Test the function with the provided test case
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]) == 2