def end_other(a, b):
    """
    Return True if either string appears at the end of the other,
    ignoring case differences. No .endswith used.
    """
    a = a.lower()
    b = b.lower()
    if len(a) >= len(b) and a[-len(b):] == b:
        return True
    if len(b) >= len(a) and b[-len(a):] == a:
        return True
    return False

print(end_other('Hiabc', 'abc'))   # True
print(end_other('AbC', 'HiaBc'))   # True
print(end_other('abc', 'abXabc'))  # True
