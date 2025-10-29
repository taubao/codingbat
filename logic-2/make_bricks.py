def make_bricks(small, big, goal):
    """
    Return True if it is possible to reach the goal length using
    small bricks (1 inch each) and big bricks (5 inches each).
    """
    max_big = goal // 5
    used_big = min(big, max_big)
    remaining = goal - used_big * 5
    return remaining <= small

print(make_bricks(3, 1, 8))   # True
print(make_bricks(3, 1, 9))   # False
print(make_bricks(3, 2, 10))  # True
