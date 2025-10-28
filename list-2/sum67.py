def sum67(nums):
    total = 0
    skip = False
    for n in nums:
        if n == 6:
            skip = True
        elif n == 7 and skip:
            skip = False
        elif not skip:
            total += n
    return total

print(sum67([1, 2, 2]))               # 5
print(sum67([1, 2, 2, 6, 99, 99, 7])) # 5
print(sum67([1, 1, 6, 7, 2]))         # 4
