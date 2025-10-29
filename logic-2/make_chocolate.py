def make_chocolate(small, big, goal):
    max_big = goal // 5
    big_used = min(max_big, big)
    remainder = goal - big_used * 5

    if remainder <= small:
        return remainder
    else:
        return -1

print(make_chocolate(4, 1, 9))   # 4
print(make_chocolate(4, 1, 10))  # -1
print(make_chocolate(4, 1, 7))   # 2
