def lucky_sum(a, b, c):
    """
    Return the sum of a, b, and c.
    However, if one of the values is 13, it does not count,
    and all values to its right do not count.
    """
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c

print(lucky_sum(1, 2, 3))   # 6
print(lucky_sum(1, 2, 13))  # 3
print(lucky_sum(1, 13, 3))  # 1
