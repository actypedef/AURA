"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""
def noprofit_noloss(cost_price, selling_price):
    # Check if there is no profit and no loss by comparing cost price and selling price
    return cost_price == selling_price

# Test the function with the provided test case
assert noprofit_noloss(1500, 1200) == False
