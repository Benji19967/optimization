import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols
from sympy.plotting import plot


def plot_line(
    m,
    b,
    xlim: tuple[int, int] | None = None,
    ylim: tuple[int, int] | None = None,
):
    x = np.linspace(-5, 5, 100)
    print(x)

    y = m * x + b

    _, ax = plt.subplots()

    plt.plot(x, y, color="red")
    plt.xlim(xlim)
    plt.ylim(ylim)

    # Move axes to be cartesian
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")

    # Hide the top and right spines
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")

    plt.show()


def plot_line_sympy(
    m_,
    b_,
    xlim: tuple[int, int] | None = None,
    ylim: tuple[int, int] | None = None,
):
    # Define symbols
    x, m, b = symbols("x m b")

    # Define the function
    y = m * x + b

    # Substitute values for m and b
    plot(y.subs({m: m_, b: b_}), (x, -5, 5), xlim=xlim, ylim=ylim, line_color="red")
