# Numerical Analysis
# Bisection Method to find roots of an equation
# With SymPy for function generalization

from sympy import *
import time
start_time = time.time()


def main():
    f = Function('f')
    x = Symbol('x')
    f = (x ** 3) + 2 * (x ** 2) + 10 * x - 20

    bisection(f, 1.0, 2.0, 0.5e-12)             # function, lower bound, upper bound, accuracy desired


def bisection(f, a, b, acc):
    x = Symbol('x')                             # set up x as symbol for functions below
    error = 10                                  # before assignment in while loop
    err = []                                    # to store errors
    made_accuracy = 0

    while error > acc:                          # if error still larger than desired accuracy

        m = (a + b) / 2                         # middle between bounds
        ans = f.evalf(subs={x: m})

        if ans > 0:
            error = abs(b - m)
            b = m

        elif ans < 0:
            error = abs(a - m)
            a = m

        err.append(error)

    print("\nNum iterations needed:", len(err))
    print("Root:", m)
    print("Execution time: %s seconds" % (time.time() - start_time))


if __name__ == "__main__":
    main()
else:
    f = Function('f')
