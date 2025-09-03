"""
Write a python function to find even numbers from a list of numbers.
assert Split([1,2,3,4,5]) == [2,4]
"""
def Split(list1):
    # Initialize an empty list to store even numbers
    ev_li = []
    
    # Iterate through each number in the input list
    for i in list1:
        # Check if the number is even
        if i % 2 == 0:
            # Append the even number to the ev_li list
            ev_li.append(i)
    
    # Return the list of even numbers
    return ev_li

# Test the function with the provided test case
assert Split([1, 2, 3, 4, 5]) == [2, 4]
