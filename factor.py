def factor(x):
    import math
    breakdown = "factorization: "
    y = 2
    while y < x:
        if x%y != 0:
            breakdown = .join(breakdown, str(x/y), "*")
            x = x/y
        else:
            y = y + 1
    if y == x:
        break
    print(breakdown - "*")


factor(27)
# introduce temporary variable y
#create a string
# start a while looop
# divide x by y until x % t != 0
# concatenating each y to string
# repeat process for increasing values of y until y > x
# print "x = string"
# possibly develop a count method to show powers in string