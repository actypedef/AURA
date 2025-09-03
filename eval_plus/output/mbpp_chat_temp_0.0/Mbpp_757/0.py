"""
Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""
def count_reverse_pairs(arr):
    # Initialize a counter for reverse pairs
    count = 0
    
    # Iterate through each word in the array
    for i in range(len(arr)):
        # Check all other words in the array
        for j in range(i + 1, len(arr)):
            # Check if the current word is the reverse of another word
            if arr[i] == arr[j][::-1]:
                # Increment the counter if it's a reverse pair
                count += 1
                
    # Return the total count of reverse pairs found
    return count

# Test the function with the provided test case
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]) == 2