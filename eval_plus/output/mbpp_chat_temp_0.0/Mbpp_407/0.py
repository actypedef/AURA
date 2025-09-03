"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""
def rearrange_bigger(n):
    # Convert the number to a list of its digits
    nums = list(str(n))
    
    # Traverse the list from right to left
    for i in range(len(nums) - 2, -1, -1):
        # If the current digit is less than the next one
        if nums[i] < nums[i + 1]:
            # Extract the part of the list that needs to be rearranged
            to_rearrange = nums[i:]
            # Find the smallest digit greater than the first digit of 'to_rearrange'
            min_greater = min(filter(lambda x: x > to_rearrange[0], to_rearrange))
            # Remove this digit from 'to_rearrange'
            to_rearrange.remove(min_greater)
            # Sort the remaining digits in ascending order
            to_rearrange.sort()
            # Reconstruct the list with the new arrangement
            nums[i:] = [min_greater] + to_rearrange
            # Return the new number as an integer
            return int("".join(nums))

# Test the function with the provided test case
assert rearrange_bigger(12) == 21