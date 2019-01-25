from prime_count import primecount

def random_polynomial(x):
    return x**2 + 3*x + 1

if __name__ == '__main__':
    n = primecount(10)

    print("Look at me, I calculated the 10th prime number - it's %i" % n)

    print("Now watch me calculate some random polynomial of the 10th prime number")

    print("Oh look, it's %i" % random_polynomial(n))
