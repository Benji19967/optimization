:q
import sympy


# TODO: clean this up and test for different function
#       try different differentiation techniques
def main():
    x = sympy.Symbol("x")
    f_prime = sympy.Derivative(x * x, evaluate=True)
    print(f_prime)


if __name__ == "__main__":
    main()
