"""
Find best line fit parameters m, b of line y = mx + b

Given points:
[0, 1]
[1, 3]

Approach: use (linear) least squares
"""

import cvxpy as cp
import numpy as np
from scipy.optimize import lsq_linear

from src.plotting import plot_line, plot_line_sympy


def least_squares_linear(p1, p2):
    """
    Minimize sum of residuals squared
    """

    def sum_residuals_squared(y1, y1_estimate, y2, y2_estimate):
        return (y1 - y1_estimate) ** 2 + (y2 - y2_estimate) ** 2

    m = cp.Variable()
    b = cp.Variable()
    obj = cp.Minimize(sum_residuals_squared(p1[1], m * p1[0] + b, p2[1], m * p2[0] + b))
    prob = cp.Problem(obj)  # type: ignore
    prob.solve()

    print(prob.status)
    print(f"f*: {prob.value}")
    print(f"m*: {m.value}")
    print(f"b*: {b.value}")

    return float(m.value), float(b.value)  # type: ignore


def least_squares_linear_scipy(p1, p2):
    """
    Note: Ax = b vs y = mx + b, not the same b.
    First is a constant vector, second a parameter.
    """
    res = lsq_linear(A=[[p1[0], 1], [p2[0], 1]], b=[p1[1], p2[1]])
    m, b = res.x
    return m, b


def main():
    p1 = [0, 1]
    p2 = [1, 3]
    m, b = least_squares_linear(p1, p2)
    m1, b1 = least_squares_linear_scipy(p1, p2)
    assert np.isclose(m, m1)
    assert np.isclose(b, b1)

    # plot_line(m, b, xlim=(-5, 5), ylim=(-5, 5))
    plot_line_sympy(m, b, xlim=(-5, 5), ylim=(-5, 5))


if __name__ == "__main__":
    main()
