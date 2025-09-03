"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""
def noprofit_noloss(cost_price, selling_price):
    # Check if the selling price is less than or equal to the cost price
    if selling_price <= cost_price:
        return True  # No profit and no loss
    else:
        return False  # There is a profit

# Test the function with the provided test case
assert noprofit_noloss(1500, 1200) == False