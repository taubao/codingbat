def no_teen_sum(a, b, c):
    """
    Return the sum of a, b, and c, treating values in the range 13..19 as 0,
    except 15 and 16 which are not treated as teens.
    """
    def fix_teen(n):
        if n in [13, 14, 17, 18, 19]:
            return 0
        return n

    return fix_teen(a) + fix_teen(b) + fix_teen(c)

print(no_teen_sum(1, 2, 3))    # 6
print(no_teen_sum(2, 13, 1))   # 3
print(no_teen_sum(2, 1, 14))   # 3
