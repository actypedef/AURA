
def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
import re

def fruit_distribution(s, n):
    # Extract numbers from the string using regular expressions
    numbers = map(int, re.findall(r'\d+', s))
    # Sum up the extracted numbers (apples and oranges)
    sum_apple_orange = sum(numbers)
    # Subtract the sum of apples and oranges from the total number of fruits to get mangoes
    mangoes = n - sum_apple_orange
    return mangoes

# Test cases