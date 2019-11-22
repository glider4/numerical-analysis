# Numerical Analysis
# Bisection Method to find roots of an equation

import time
start_time = time.time()


def main():
    bisection(1.0, 2.0, 0.5e-12)    # lower bound, upper bound, accuracy desired


def function(x):                    # function we're trying to find root of
    return (x ** 3) + 2 * (x ** 2) + 10 * x - 20


def bisect_bounds(a, b):
    return (a + b) / 2              # middle between bounds


def bisection(a, b, acc):

    err = []                        # to store errors
    f = 100                         # before assignment

    while abs(f) > acc:             # if desired accuracy not reached yet

        m = bisect_bounds(a, b)
        f = function(m)

        if f > 0:
            err.append(abs(b - m))
            b = m

        elif f < 0:
            err.append(abs(a - m))
            a = m

    print("\nNum iterations needed:", len(err))
    print("Root:", m)
    print("Execution time: %s seconds" % (time.time() - start_time))


if __name__ == "__main__":
    main()
else:
    print("Imported module, available function: bisection(a, b, acc)")
