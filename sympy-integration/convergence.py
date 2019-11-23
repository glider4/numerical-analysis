# Testing convergence of both schemes
# Had to generalize the functions, so using SymPy
#   Both schemes be optimized further by setting the
#   bounds [a,b] for Bisection, and setting the initial
#   guess for Newton-Raphson.  Right now I used [-10,10]
#   and 0.

from sympy import Function, Symbol
from sympy.plotting import plot
from bisection import bisection
from newton_raphson import newton


def main():
    x = Symbol('x')
    f = Function('f')

    f = 6*x**3 + 4*x**2 + x + 1         # Enter function to find roots here

    print("\nFunction to find roots of:", f)
    print("=====================================\n")

    print("Bisection results:")
    bisection(f, -10, 10, 0.5e-12)

    print("\n=====================================\n")

    print("Newton-Raphson results:")
    newton(f, 0, 0.5e-12)

    print("\n=====================================")

    plot(f)

if __name__ == '__main__':
    main()
