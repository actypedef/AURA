

def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
def car_race_collision(n: int) -> int:
    """
    Calculate the total number of collisions between two sets of n cars each,
    one set driving left to right and the other set driving right to left on an infinite straight road.
    
    Args:
    n (int): The number of cars in each direction.
    
    Returns:
    int: The total number of collisions.
    """
    # Since every car going in one direction will eventually collide with every car coming from the opposite direction,
    # the total number of collisions is simply the product of the number of cars in each direction.
    return n * n

# Test cases to verify the correctness of the function
assert car_race_collision(0) == 0, "No cars means no collisions."
assert car_race_collision(1) == 1, "One car from each side results in one collision."
assert car_race_collision(2) == 4, "Two cars from each side result in four collisions."
assert car_race_collision(3) == 9, "Three cars from each side result in nine collisions."
