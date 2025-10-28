def big_diff(nums):
    """
    Given an array length 1 or more of ints, return the difference between
    the largest and smallest values in the array.
    """
    return max(nums) - min(nums)

print(big_diff([10, 3, 5, 6]))  # 7
print(big_diff([7, 2, 10, 9]))  # 8
print(big_diff([2, 10, 7, 2]))  # 8
