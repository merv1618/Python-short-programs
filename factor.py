# I wrote a short program which factors positive integers

def factor(x):
    breakdown = ""
   # final list of prime numbers
    y = 2
   # lowest prime
    while y <= x:
        if x%y == 0:
            breakdown = breakdown + "*" + str(y)
            # concatenates instance of prime number to final list
            x = x/y
            # repeatedly tests the same prime number
            # removes need to account for composite integers
        else:
            y = y + 1
    if y > x:
        print(breakdown[1:])
    # removes the unnecessary asterisk
