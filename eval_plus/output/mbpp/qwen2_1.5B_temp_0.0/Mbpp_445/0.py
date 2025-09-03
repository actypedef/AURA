"""
Write a function to perform index wise multiplication of tuple elements in the given two tuples.
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""
def index_multiplication(tuple1, tuple2):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the indices of both tuples
    for i in range(len(tuple1)):
        # Multiply the corresponding elements from both tuples and append to the result list
        result.append((tuple1[i][0] * tuple2[i][0], tuple1[i][1] * tuple2[i][1]))
    
    # Return the resulting list of tuples
    return result

# Test the function with the provided test case
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))