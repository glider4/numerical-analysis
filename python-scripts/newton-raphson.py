# Numerical Analysis
# Newton-Raphson Method to find roots of an equation
# Uses derivative of equation in iterative scheme

import time
start_time = time.time()


def main():
    newton(0, 0.5e-12)              # guess where root is, accuracy desired


def function(x):                    # function we're trying to find root of
    return (x ** 3) + 2 * (x ** 2) + 10 * x - 20


def function_prime(x):              # derivative of function we're trying to find root of
    return (3 * (x ** 2)) + (4 * x) + 10


def newton(guess, acc):

    err = []                        # to store errors
    x = guess
    made_accuracy = 0           # program has not achieved proper accuracy yet

    while made_accuracy == 0:    # if desired accuracy not reached yet

        x_1 = x - (function(x) / function_prime(x))

        error = abs(x_1 - x)
        err.append(error)

        if error < acc:
            made_accuracy = 1
        else:
            x = x_1


    print("\nNum iterations needed:", len(err))
    print("Root:", x)
    print("Execution time: %s seconds" % (time.time() - start_time))


if __name__ == "__main__":
    main()
else:
    print("Imported module, available function: newton(guess, acc)")
