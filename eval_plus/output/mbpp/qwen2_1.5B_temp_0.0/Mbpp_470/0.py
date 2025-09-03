"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""
def add_pairwise(input_tuple):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over the input tuple using range(len(input_tuple) - 1)
    for i in range(len(input_tuple) - 1):
        # Calculate the sum of the current element and the next one
        pair_sum = input_tuple[i] + input_tuple[i+1]
        
        # Append the calculated sum to the result list
        result.append(pair_sum)
    
    # Return the resulting list
    return result

# Test the function with the provided test case
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)