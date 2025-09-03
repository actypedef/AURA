"""
Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""
def count_reverse_pairs(arr):
    # Create a set to store unique strings
    s = set(arr)
    
    # Initialize count of reverse pairs
    count = 0
    
    # Iterate through each string in the array
    for i in arr:
        # Check if the reverse of the string exists in the set and is not the same as the original
        if i[::-1] in s and i != i[::-1]:
            count += 1
    
    # Each pair is counted twice, so divide by 2
    return count // 2

# Test the function with the provided test case
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]) == 2
