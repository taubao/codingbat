def monkey_trouble(a_smile, b_smile):
    """
    We are in trouble if both monkeys are smiling or if neither is smiling.
    Return True if we are in trouble.
    """
    return a_smile == b_smile

print(monkey_trouble(True, True))    # True
print(monkey_trouble(False, False))  # True
print(monkey_trouble(True, False))   # False