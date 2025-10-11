import cvxpy as cp
import numpy as np


def lp_1():
    x = cp.Variable()
    constraints = [x >= 0, x <= 1]
    obj = cp.Minimize(x - 1)
    prob = cp.Problem(obj, constraints)
    prob.solve()

    print(prob.status)
    print(f"f*: {prob.value}")
    print(f"x*: {x.value}")


def lp_2():
    t = cp.Variable()
    x = cp.Variable()
    constraints = [cp.abs(x) <= t]
    obj = cp.Minimize(t)
    prob = cp.Problem(obj, constraints)
    prob.solve()

    print(prob.status)
    print(f"f*: {prob.value:.1f}")
    print(f"x*: {x.value:.1f}")
    print(f"t*: {t.value:.1f}")


def lp_3():
    x1 = cp.Variable()
    x2 = cp.Variable()
    f = cp.hstack([2 * x1 + 3 * x2, -3 * x1])
    obj = cp.Minimize(cp.norm_inf(f))
    constraints = [
        cp.abs(x1 - 2 * x2 - 2) <= 1,
    ]
    prob = cp.Problem(obj, constraints)
    prob.solve(verbose=True)

    print(prob.status)
    print(f"f*: {prob.value:.2f}")
    print(f"x1*: {x1.value:.2f}")
    print(f"x2*: {x2.value:.2f}")


def main():
    # lp_1()
    # lp_2()
    lp_3()


if __name__ == "__main__":
    main()
