# Optimization

## So, what is optimization?

From what I currently know: 
  - Finding the minimum of a function
  - Curve fitting:
      - adjust the coefficients of a function to minimize (or maximize) a metric (possibly given a set of constraints).
        - the set of coefficients is the solution we are looking for and called the __argmin__

## What is the simplest (non-trivial) optimization problem I can come up with?

### Example 1

- f: {0, 1} -> {5, 10}
 - the minimum value of f is 5 and the __argmin__ is 0

- How could I solve this algorithmically?
  - Scan the input set and keep track of the min output value.
    - Time: O(n) where n: num elements in input set

### Example 2

- f(x) = <some unkown function> where x is in the interval [0, 1] of real values.
  - Problem: I cannot just scan the input set as there are infinitely many values. 
  - Possible solutions:
    - I could sample f(x) for a few x values and see which one is minimal and hopefully be at a local minimum.
      - Problem: I have no idea how the function looks like 
        - f(0.001) could be 1000
        - f(0.002) could be -2500
    - Use derivatives to find direction of descent -- gradient descent.
      - How do I programatically take derivatives of a function?

## Programatically taking derivaties of a function

- Symbolic derivativation using a library
