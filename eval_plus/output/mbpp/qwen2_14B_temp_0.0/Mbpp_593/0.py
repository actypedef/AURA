"""
Write a function to remove leading zeroes from an ip address.
assert removezero_ip("216.08.094.196")==('216.8.94.196')
"""
import re

def removezero_ip(ip):
    # Use regex to find leading zeroes in each segment of the IP address
    result = re.sub(r'(^0+(\D))|((\D)0+(?=\D))', r'\4', ip)
    return result

# Test the function with the provided test case
assert removezero_ip("216.08.094.196") == '216.8.94.196'
