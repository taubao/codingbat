def string_bits(str):
    """
    Given a string, return a new string made of every other char starting with the first.
    """
    return str[::2]

print(string_bits('Hello'))      # Hlo
print(string_bits('Hi'))         # H
print(string_bits('Heeololeo'))  # Hello
