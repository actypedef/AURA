"""
Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""
def count_reverse_pairs(arr):
    # Initialize a counter for reverse pairs
    count = 0
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Check if the current element is a reverse of any other element in the array
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j][::-1]:
                count += 1
                
    return count

# Test the function with the provided test case
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]) == 2
