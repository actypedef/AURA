"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
"""
def sum_list(list1, list2):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over the elements of both lists simultaneously using zip()
    for a, b in zip(list1, list2):
        # Append the sum of corresponding elements to the result list
        result.append(a + b)
    
    return result

# Test the function with the provided test case
assert sum_list([10, 20, 30], [15, 25, 35]) == [25, 45, 65]
