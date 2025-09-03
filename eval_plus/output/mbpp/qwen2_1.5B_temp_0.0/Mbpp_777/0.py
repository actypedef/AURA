"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""
def find_sum(lst):
    # Create a dictionary to count occurrences of each element
    count_dict = {}
    
    # Count occurrences of each element in the list
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Calculate the sum of non-repeated elements
    total_sum = 0
    for num, count in count_dict.items():
        if count == 1:
            total_sum += num
    
    return total_sum

# Test the function with the provided test case
assert find_sum([1,2,3,1,1,4,5,6]) == 21