"""
Write a function to remove leading zeroes from an ip address.
assert removezero_ip("216.08.094.196")==('216.8.94.196')
"""
def removezero_ip(ip):
    # Split the IP address into its components
    parts = ip.split('.')
    
    # Remove leading zeros from each part
    cleaned_parts = [part.lstrip('0') for part in parts]
    
    # Join the cleaned parts back together into a single string
    cleaned_ip = '.'.join(cleaned_parts)
    
    return cleaned_ip

# Test cases to verify the correctness of the solution
assert removezero_ip("226.08.094.196") == ('226.8.94.196')
assert removezero_ip("000.000.000.000") == ('0.0.0.0')
assert removezero_ip("123.45.67.89") == ('123.45.67.89')
assert removezero_ip("0000.0000.0000.0000") == ('0.0.0.0')