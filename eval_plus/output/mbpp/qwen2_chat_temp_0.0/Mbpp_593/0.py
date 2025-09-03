"""
Write a function to remove leading zeroes from an ip address.
assert removezero_ip("216.08.094.196")==('216.8.94.196')
"""
def removezero_ip(ip):
    # Split the IP address into its components using '.' as the delimiter
    ip = ip.split('.')
    
    # Convert each component to an integer and then back to string to remove any leading zeros
    ip = [str(int(i)) for i in ip]
    
    # Join the modified components back together using '.' as the delimiter
    return '.'.join(ip)

# Test the function with the provided test case
assert removezero_ip("216.08.094.196") == '216.8.94.196'
