def front_back(str):
    """
    Given a string, return a new string where the first and last characters have been exchanged.
    """
    if len(str) <= 1:
        return str
    return str[-1] + str[1:-1] + str[0]

print(front_back('code'))  # 'eodc'
print(front_back('a'))     # 'a'
print(front_back('ab'))    # 'ba'
