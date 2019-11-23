# Numerical Analysis
# Newton-Raphson Method to find roots of an equation
# Uses derivative of equation in iterative scheme

from sympy import *
import time
start_time = time.time()


def main():
    f = Function('f')
    x = Symbol('x')
    f = (x ** 3) + 2 * (x ** 2) + 10 * x - 20

    newton(f, 2, 0.5e-12)           # function, guess where root is, accuracy desired


def newton(f, g, acc):
    x = Symbol('x')                 # set up x as symbol for functions below
    f_prime = diff(f)               # derivative of inputted function
    err = []                        # to store errors
    made_accuracy = 0               # (flag) program has not achieved proper accuracy yet

    while made_accuracy == 0:       # if desired accuracy not reached yet

        g_1 = g - (f.evalf(subs={x: g}) / f_prime.evalf(subs={x: g}))

        error = abs(g_1 - g)
        err.append(error)

        if error < acc:
            made_accuracy = 1       # signal flag to end computation if accuracy has been reached
        else:
            g = g_1                 # otherwise, continue iterating

    print("\nNum iterations needed:", len(err))
    print("Root:", g)
    print("Execution time: %s seconds" % (time.time() - start_time))


if __name__ == "__main__":
    main()
else:
    f = Function('f')
