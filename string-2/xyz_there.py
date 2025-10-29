def xyz_there(str):
    """
    Return True if 'xyz' appears in the string not directly
    preceded by a period.
    """
    for i in range(len(str) - 2):
        if str[i:i+3] == 'xyz':
            if i == 0 or str[i-1] != '.':
                return True
    return False


print(xyz_there('abcxyz'))     # True
print(xyz_there('abc.xyz'))    # False
print(xyz_there('xyz.abc'))    # True
