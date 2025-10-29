def last2(str):
    """
    Given a string, return the count of the number of times that a substring length 2 
    appears in the string and also as the last 2 chars of the string, 
    not counting the end substring itself.
    """
    if len(str) < 2:
        return 0

    last2_sub = str[-2:]
    count = 0

    for i in range(len(str) - 2):
        if str[i:i+2] == last2_sub:
            count += 1

    return count

print(last2('hixxhi'))      # 1
print(last2('xaxxaxaxx'))   # 1
print(last2('axxxaaxx'))    # 2
