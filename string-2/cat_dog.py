def cat_dog(str):
    return str.count('cat') == str.count('dog')

print(cat_dog('catdog'))          # True
print(cat_dog('catcat'))          # False
print(cat_dog('1cat1cadodog'))    # True
