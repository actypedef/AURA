"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""
def rearrange_bigger(num):
    # Convert the number to a list of its digits
    num = list(str(num))
    
    # Traverse the list from right to left
    for i in range(len(num) - 2, -1, -1):
        # If the current digit is less than the next digit
        if num[i] < num[i + 1]:
            # Extract the part of the list that needs to be sorted
            temp_list = num[i:]
            # Sort this part in ascending order
            temp_list.sort()
            # Replace the original part with the sorted version
            num[i:] = temp_list
            # Find the first digit greater than the current digit
            for j in range(i + 1, len(num)):
                if num[j] > num[i]:
                    # Swap these two digits
                    num[i], num[j] = num[j], num[i]
                    # Return the new number as an integer
                    return int(''.join(num))
    # If no such arrangement exists, return -1
    return -1

# Test the function with the provided test case
assert rearrange_bigger(12) == 21