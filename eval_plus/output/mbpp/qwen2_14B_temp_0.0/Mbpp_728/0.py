"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
"""
def sum_list(lst1, lst2):
    # Initialize an empty list to store the sums
    res = []
    
    # Iterate through the elements of both lists simultaneously
    for i in range(len(lst1)):
        # Calculate the sum of corresponding elements and append to the result list
        res.append(lst1[i] + lst2[i])
    
    return res

# Test the function with the provided test case
assert sum_list([10, 20, 30], [15, 25, 35]) == [25, 45, 65]
