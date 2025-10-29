def near_ten(num):
    """
    Return True if num is within 2 of a multiple of 10.
    """
    mod = num % 10
    return mod <= 2 or mod >= 8

print(near_ten(12))  # True
print(near_ten(17))  # False
print(near_ten(19))  # True
