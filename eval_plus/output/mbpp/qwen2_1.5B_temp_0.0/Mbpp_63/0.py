"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""
def max_difference(pairs):
    # Sort the pairs based on the second element of each pair
    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    
    # Initialize the maximum difference to zero
    max_diff = 0
    
    # Iterate through the sorted pairs starting from the second one
    for i in range(1, len(sorted_pairs)):
        # Calculate the difference between the current pair and the previous one
        diff = sorted_pairs[i][1] - sorted_pairs[i-1][1]
        
        # Update the maximum difference if the current difference is greater
        if diff > max_diff:
            max_diff = diff
    
    return max_diff

# Test the function with the provided data point
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7