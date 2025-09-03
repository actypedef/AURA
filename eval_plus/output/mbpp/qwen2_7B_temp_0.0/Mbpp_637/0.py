"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""
def noprofit_noloss(cost_price, selling_price):
    # Check if the cost price is less than or equal to zero
    if cost_price <= 0:
        return False
    
    # Calculate the profit percentage
    profit_percentage = ((selling_price - cost_price) / cost_price) * 100
    
    # Check if there is no profit (profit percentage is less than or equal to zero)
    if profit_percentage <= 0:
        return True
    
    return False

# Test the function with the provided test case
assert noprofit_noloss(1500, 1200) == False