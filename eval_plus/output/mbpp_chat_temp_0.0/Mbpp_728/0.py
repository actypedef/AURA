"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
"""
def sum_list(list1, list2):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over the indices of the lists using enumerate
    for i in range(len(list1)):
        # Append the sum of corresponding elements from both lists to the result list
        result.append(list1[i] + list2[i])
    
    # Return the resulting list containing sums of corresponding elements
    return result

# Test the function with the provided test case
assert sum_list([10, 20, 30], [15, 25, 35]) == [25, 45, 65]
