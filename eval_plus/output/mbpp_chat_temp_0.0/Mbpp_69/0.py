"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""
def is_sublist(main_list, sub_list):
    # Check if the sub_list is empty or equal to the main_list
    if sub_list == [] or sub_list == main_list:
        return True
    # Check if the length of sub_list is greater than main_list
    elif len(sub_list) > len(main_list):
        return False
    else:
        # Iterate through the main_list to find the start of the sub_list
        for i in range(len(main_list)):
            if main_list[i] == sub_list[0]:
                n = 1
                # Continue checking subsequent elements
                while (n < len(sub_list)) and (main_list[i + n] == sub_list[n]):
                    n += 1
                # If all elements match, return True
                if n == len(sub_list):
                    return True
    # If no match found, return False
    return False

# Test the function with the provided test case
assert is_sublist([2, 4, 3, 5, 7], [3, 7]) == False