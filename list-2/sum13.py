def sum13(nums):
    """
    Return the sum of the numbers in the array, returning 0 for an empty array.
    The number 13 is unlucky, so it does not count, and numbers immediately after 13 also do not count.
    """
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1
    return total

print(sum13([1, 2, 2, 1]))     # 6
print(sum13([1, 1]))           # 2
print(sum13([1, 2, 2, 1, 13])) # 6
print(sum13([13, 1, 2, 13, 2]))# 0
