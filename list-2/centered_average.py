def centered_average(nums):
    """
    Return the "centered" average of an array of ints, which is the mean
    average of the values, ignoring the largest and smallest value.
    Use integer division for the result.
    """
    return (sum(nums) - max(nums) - min(nums)) // (len(nums) - 2)

print(centered_average([1, 2, 3, 4, 100]))       # 3
print(centered_average([1, 1, 5, 5, 10, 8, 7]))  # 5
print(centered_average([-10, -4, -2, -4, -2, 0]))# -3
