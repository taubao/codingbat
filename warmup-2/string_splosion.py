def string_splosion(str):
    """
    Given a non-empty string like 'Code', return a string like 'CCoCodCode'.
    """
    result = ''
    for i in range(len(str)):
        result += str[:i+1]
    return result

print(string_splosion('Code'))  # CCoCodCode
print(string_splosion('abc'))   # aababc
print(string_splosion('ab'))    # aab
