def without_end(str):
    """
    Given a string, return a version without the first and last char,
    so "Hello" yields "ell". The string length will be at least 2.
    """
    return str[1:-1]

print(without_end('Hello'))   # ell
print(without_end('java'))    # av
print(without_end('coding'))  # odin
