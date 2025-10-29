def caught_speeding(speed, is_birthday):
    """
    You are driving a little too fast, and a police officer stops you.
    Return 0 for no ticket, 1 for a small ticket, and 2 for a big ticket.
    On your birthday, your speed can be 5 higher in all cases.
    """
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2

print(caught_speeding(60, False))  # 0
print(caught_speeding(65, False))  # 1
print(caught_speeding(65, True))   # 0
