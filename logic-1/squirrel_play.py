def squirrel_play(temp, is_summer):
    """
    The squirrels in Palo Alto play if the temperature is between 60 and 90 (inclusive),
    except in summer when the upper limit is 100 instead of 90.
    Return True if the squirrels play, False otherwise.
    """
    upper = 100 if is_summer else 90
    return 60 <= temp <= upper

print(squirrel_play(70, False))  # True
print(squirrel_play(95, False))  # False
print(squirrel_play(95, True))   # True
