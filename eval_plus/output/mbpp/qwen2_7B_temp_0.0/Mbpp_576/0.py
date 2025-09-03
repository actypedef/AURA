"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""
def is_Sub_Array(arr1, arr2):
    # Check if arr2 is empty or arr2 is equal to arr1
    if (len(arr2) == 0):
        return True
    if (len(arr2) > len(arr1)):
        return False

    # Iterate through arr1 to find a match for arr2
    for i in range(len(arr1)):
        if arr1[i] == arr2[0]:
            j = 1
            while (j < len(arr2)) and (arr1[i + j] == arr2[j]):
                j += 1

            # If all elements of arr2 are found in arr1
            if (j == len(arr2)):
                return True

    return False

# Test the function with the provided test case
assert is_Sub_Array([1, 4, 3, 5], [1, 2]) == False