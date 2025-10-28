def sum_double(a, b):
    """
    Given two int values, return their sum.
    Unless the two values are the same, then return double their sum.
    """
    if a == b:
        return 2 * (a + b)
    else:
        return a + b

print(sum_double(1, 2))  # 3
print(sum_double(3, 2))  # 5
print(sum_double(2, 2))  # 8
