def sorta_sum(a, b):
    """
    Given 2 ints, a and b, return their sum.
    However, if the sum is in the range 10..19 inclusive, return 20 instead.
    """
    total = a + b
    if 10 <= total <= 19:
        return 20
    return total

print(sorta_sum(3, 4))    # 7
print(sorta_sum(9, 4))    # 20
print(sorta_sum(10, 11))  # 21
