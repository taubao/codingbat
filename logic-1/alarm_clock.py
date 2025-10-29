def alarm_clock(day, vacation):
    """
    Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ..., 6=Sat, 
    and a boolean indicating if we are on vacation, 
    return a string indicating when the alarm should ring.
    
    Weekdays: "7:00", Weekends: "10:00".
    On vacation: weekdays -> "10:00", weekends -> "off".
    """
    if vacation:
        if 1 <= day <= 5:
            return "10:00"
        else:
            return "off"
    else:
        if 1 <= day <= 5:
            return "7:00"
        else:
            return "10:00"

print(alarm_clock(1, False))  # '7:00'
print(alarm_clock(5, False))  # '7:00'
print(alarm_clock(0, False))  # '10:00'
