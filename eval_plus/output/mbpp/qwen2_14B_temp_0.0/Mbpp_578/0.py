"""
Write a function to interleave 3 lists of the same length into a single flat list.
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
"""
def interleave_lists(list1, list2, list3):
    # Initialize an empty list to store the interleaved result
    result = []
    
    # Iterate through the indices of the lists
    for i in range(len(list1)):
        # Append elements from each list at index i to the result list
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])
    
    return result

# Test the function with the provided test case
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]) == [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
