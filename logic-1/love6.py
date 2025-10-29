def love6(a, b):
    """
    Return True if either a or b is 6, or if their sum or absolute difference is 6.
    """
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

print(love6(6, 4))  # True
print(love6(4, 5))  # False
print(love6(1, 5))  # True
