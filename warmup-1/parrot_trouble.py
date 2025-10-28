def parrot_trouble(talking, hour):
    """
    We are in trouble if the parrot is talking and the hour is before 7 or after 20.
    Return True if we are in trouble.
    """
    return talking and (hour < 7 or hour > 20)

print(parrot_trouble(True, 6))   # True
print(parrot_trouble(True, 7))   # False
print(parrot_trouble(False, 6))  # False
