"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""
def noprofit_noloss(cost_price, selling_price):
    # Check if the cost price is equal to the selling price
    if (cost_price == selling_price):
        return True
    else:
        return False

# Test the function with the provided test case
assert noprofit_noloss(1500, 1200) == False