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


def lp_3(verbose=True):
    """
    minimize norm_inf(2*x1 + 3*x2, -3*x1)
    subject to |x1 - 2*x2 - 2| <= 1
    """
    x1 = cp.Variable()
    x2 = cp.Variable()
    f = cp.hstack([2 * x1 + 3 * x2, -3 * x1])
    obj = cp.Minimize(cp.norm_inf(f))
    constraints = [
        cp.abs(x1 - 2 * x2 - 2) <= 1,
    ]
    prob = cp.Problem(obj, constraints)
    prob.solve(verbose=verbose)

    print(prob.status)
    print(f"f*: {prob.value:.2f}")
    print(f"x1*: {x1.value:.2f}")
    print(f"x2*: {x2.value:.2f}")


def lp_4(verbose=True):
    """
    Equivalent to lp_3 but such that we have:
        - All variables live in domain R+
            - (make x1 = x1p - x1m, where x1p, x1m live in R+)
        - no inequlity constraints exept variabl >= 0
            - (turn '<=' to '==' via slack variables)
    """
    x1p = cp.Variable()
    x1m = cp.Variable()
    x2p = cp.Variable()
    x2m = cp.Variable()
    s1 = cp.Variable()
    s2 = cp.Variable()
    s3 = cp.Variable()
    s4 = cp.Variable()
    s5 = cp.Variable()
    s6 = cp.Variable()
    t = cp.Variable()
    variables = [x1p, x1m, x2p, x2m, s1, s2, s3, s4, s5, s6, t]

    obj = cp.Minimize(t)
    constraints = [
        2 * (x1p - x1m) + 3 * (x2p - x2m) - t + s1 == 0,
        -(2 * (x1p - x1m) + 3 * (x2p - x2m)) - t + s2 == 0,
        -3 * (x1p - x1m) - t + s3 == 0,
        -(-3 * (x1p - x1m)) - t + s4 == 0,
        (x1p - x1m) - 2 * (x2p - x2m) - 2 - 1 + s5 == 0,
        -((x1p - x1m) - 2 * (x2p - x2m) - 2) - 1 + s6 == 0,
        x1p >= 0,
        x1m >= 0,
        x2p >= 0,
        x2m >= 0,
        s1 >= 0,
        s2 >= 0,
        s3 >= 0,
        s4 >= 0,
        s5 >= 0,
        s6 >= 0,
    ]
    prob = cp.Problem(obj, constraints)
    prob.solve(verbose=verbose)

    print(prob.status)
    print(f"f*: {prob.value:.2f}")
    print(f"x1: {x1p.value - x1m.value:.2f}")
    print(f"x2: {x2p.value - x2m.value:.2f}")

    print(f"x1p: {x1p.value:.2f}")
    print(f"x1m: {x1m.value:.2f}")
    print(f"x2p: {x2p.value:.2f}")
    print(f"x2m: {x2m.value:.2f}")
    print(f"s1: {s1.value:.2f}")
    print(f"s2: {s2.value:.2f}")
    print(f"s3: {s3.value:.2f}")


def main():
    verbose = False
    # lp_1()
    # lp_2()

    lp_3(verbose)
    lp_4(verbose)


if __name__ == "__main__":
    main()
