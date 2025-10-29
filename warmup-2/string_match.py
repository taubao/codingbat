def string_match(a, b):
    """
    Given 2 strings, a and b, return the number of positions where they contain
    the same length 2 substring.
    """
    shorter = min(len(a), len(b))
    count = 0
    
    for i in range(shorter - 1):
        a_sub = a[i:i+2]
        b_sub = b[i:i+2]
        if a_sub == b_sub:
            count += 1

    return count

print(string_match('xxcaazz', 'xxbaaz'))  # 3
print(string_match('abc', 'abc'))         # 2
print(string_match('abc', 'axc'))         # 0
