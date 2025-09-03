"""
Write a function to remove leading zeroes from an ip address.
assert removezero_ip("216.08.094.196")==('216.8.94.196')
"""
def removezero_ip(ip):
    # Split the IP address into its components using the dot separator
    parts = ip.split('.')
    
    # Convert each component to an integer and back to a string to remove leading zeros
    cleaned_parts = [str(int(part)) for part in parts]
    
    # Join the cleaned components back together with dots
    return '.'.join(cleaned_parts)

# Test the function with the provided test case
assert removezero_ip("216.08.094.196") == '216.8.94.196'
