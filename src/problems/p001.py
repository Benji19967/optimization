"""
minimize x
subject to x >= 5
"""

import cvxpy as cp


def main():
    x = cp.Variable()
    obj = cp.Minimize(x)
    constraints = [x >= 5]
    prob = cp.Problem(obj, constraints)  # type: ignore
    prob.solve()

    print(prob.status)
    print(f"f*: {prob.value}")
    print(f"x*: {x.value}")


if __name__ == "__main__":
    main()
