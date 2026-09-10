"""David Evra - Homework 1, Problem 1: Quadratic Equations."""

from math import pow, sqrt
import matplotlib.pyplot as plt


def get_variable(v: str) -> float | None:
    """Requests for a coefficient and converts it to a float."""
    vStr = input(f"Enter {v}: ")

    # Returns None if user Enters an empty string.
    if vStr == "": 
        return None
    
    return float(vStr)

def discriminant(a: float, b: float, c: float) -> float:
    """Calculates the discriminant"""
    return float(pow(b, 2) - (4 * a * c))

def show_solution(a: float, b: float, d: float):
    """Displays all real solutions."""
    if d < 0:
        print('no real solutions')
    else:
        # Only calculates quadratic formula when discriminant is not negative.
        x1, x2 = quadratic_formula(a, b, d)

        # d = zero only needs 1 root due to both roots are equal.
        if d == 0:
            print(f'one solution: {x1:.5f}')
        else:
            print(f'two solutions: x1={x1:.5f} x2={x2:.5f}')

def quadratic_formula(a: float, b: float, d: float) -> tuple[float, float]:
    """Calculates both roots using a nonnegative discriminant."""
    x_1 = (-b + sqrt(d)) / (2 * a)
    x_2 = (-b - sqrt(d)) / (2 * a)

    # Returns roots from least to greatest.
    return tuple(sorted((x_1, x_2)))

def plot_quadratic(a: float, b: float, c: float, d: float):
    """Dras the quadratic function."""
    if d < 0:
        # Centers interval on the parabola's vertex when there is no real solutions.
        x_center = -b / (2 * a)

        x_min = x_center - 2
        x_max = x_center + 2
    else:
        x_1, x_2 = quadratic_formula(a, b, d)

        # Increaces intervals by two units beyond each root.
        x_min = x_1 - 2
        x_max = x_2 + 2

    step = (x_max - x_min) / 149

    # Generates x-values and calculate the matching y-values.
    x = [x_min + i * step for i in range(150)]
    y = [a*pow(x, 2) + b*x + c for x in x]

    plt.plot(x, y)
    plt.show()

def main():
    """Read coefficients and displays solutions and graph each equation."""
    while True:
        a = get_variable('a')
        if a == None:
            break

        b = get_variable('b')
        c = get_variable('c')
        d = discriminant(a, b, c)

        show_solution(a, b, d)
        plot_quadratic(a, b, c, d)


if __name__ == "__main__":
    main()