def first_half(str):
    """
    Given a string of even length, return the first half.
    So the string "WooHoo" yields "Woo".
    """
    return str[:len(str)//2]

print(first_half('WooHoo'))      # Woo
print(first_half('HelloThere'))  # Hello
print(first_half('abcdef'))      # abc