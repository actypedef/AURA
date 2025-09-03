
def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """
def move_one_ball(arr):
    # Check if the array is empty or has only one element
    if len(arr) <= 1:
        return True
    
    # Find the number of shifts needed to sort the array
    shifts = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            shifts += 1
            start_index = (i + 1) % n
    
    # If there's more than one place where the sequence breaks, it cannot be sorted
    if shifts > 1:
        return False
    
    # If there's exactly one break, check if it's at the end of the array
    elif shifts == 1:
        return arr[start_index:] + arr[:start_index] == sorted(arr)
    
    # If no breaks, the array is already sorted
    return True

# Test cases