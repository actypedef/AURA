"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""
def max_product_tuple(tuples_list):
    # Initialize the maximum product to negative infinity
    max_product = float('-inf')
    
    # Iterate through each tuple in the list
    for tup in tuples_list:
        # Calculate the product of the two elements in the tuple
        product = tup[0] * tup[1]
        
        # Update the maximum product if the current product is greater
        if product > max_product:
            max_product = product
    
    # Return the maximum product found
    return max_product

# Test the function with the provided data point
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36