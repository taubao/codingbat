def date_fashion(you, date):
    """
    You and your date are trying to get a table at a restaurant.
    If either of you has style 8 or more, then the result is 2 (yes).
    If either of you has style 2 or less, then the result is 0 (no).
    Otherwise, the result is 1 (maybe).
    """
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

print(date_fashion(5, 10))  # 2
print(date_fashion(5, 2))   # 0
print(date_fashion(5, 5))   # 1
