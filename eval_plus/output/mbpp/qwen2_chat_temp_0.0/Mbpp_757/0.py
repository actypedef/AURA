"""
Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""
def count_reverse_pairs(str_list):
    # Initialize a counter for reverse pairs
    count = 0
    
    # Iterate over each string in the list
    for i in range(len(str_list)):
        # Check all other strings in the list
        for j in range(i + 1, len(str_list)):
            # If the current string is the reverse of another string
            if str_list[i] == str_list[j][::-1]:
                # Increment the counter
                count += 1
                
    # Return the total count of reverse pairs
    return count

# Test the function with the provided test case
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]) == 2