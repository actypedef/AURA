"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""
def noprofit_noloss(amount_in, amount_out):
    """
    Check if there is no profit or loss.

    Args:
    amount_in (int): The amount of money received.
    amount_out (int): The amount of money spent.

    Returns:
    bool: True if there is no profit or loss, False otherwise.
    """
    return amount_in == amount_out

# Test cases
assert noprofit_noloss(1500, 1200) == False
assert noprofit_noloss(3000, 3000) == True
assert noprofit_noloss(2000, 4000) == False
assert noprofit_noloss(750, 750) == True
assert noprofit_noloss(900, 800) == False