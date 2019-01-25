import sys

def primecount(x):
    """Calculate the xth prime number"""
    count = 0
    y = 2
    while count < x:
        z = 2
        while z <= y:
            if y % z == 0 and y != z:
                y += 1
                z = 2
            elif y % z != 0:
                z += 1
            else:
                count += 1
                if count == x:
                    break
                else:
                    y += 1
                    z = 2

    return y


if __name__ == '__main__':
    # Get user input for x
    x = int(sys.argv[1])

    # Print the xth prime number
    if 10 % x == 1:
        print("The " + str(x) + "st prime number is " + str(y) + ".")
    elif 10 % x == 2:
        print("The " + str(x) + "nd prime number is " + str(y) + ".")
    elif 10 % x == 3:
        print("The " + str(x) + "rd prime number is " + str(y) + ".")
    else:
        print("The " + str(x) + "th prime number is " + str(y) + ".")
