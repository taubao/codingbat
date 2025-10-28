def sum2(nums):
    """
    Given an array of ints, return the sum of the first 2 elements in the array.
    If the array length is less than 2, just sum up the elements that exist,
    returning 0 if the array length is 0.
    """
    return sum(nums[:2])

print(sum2([1, 2, 3]))   # 3
print(sum2([1, 1]))      # 2
print(sum2([1, 1, 1, 1]))# 2
print(sum2([]))          # 0
