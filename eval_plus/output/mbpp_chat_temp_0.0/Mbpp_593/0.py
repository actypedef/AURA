"""
Write a function to remove leading zeroes from an ip address.
assert removezero_ip("216.08.094.196")==('216.8.94.196')
"""
def removezero_ip(ip):
    # Split the IP address into its components using the dot as a delimiter
    ip = ip.split('.')
    
    # Convert each component to an integer, then back to a string without leading zeros
    ip = [str(int(i)) for i in ip]
    
    # Join the modified components back together using dots as delimiters
    return '.'.join(ip)

# Test the function with the provided test case
assert removezero_ip("216.08.094.196") == '216.8.94.196'
