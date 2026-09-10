"""David Evra - Homework 1, Problem 1: Quadratic Equations."""

from math import pow, sqrt
import matplotlib.pyplot as plt


def get_variable(v: str) -> float | None:
    vStr = input(f"Enter {v}: ")
    if vStr == "":
        return None
    
    return float(vStr)

def discriminant(a: float, b: float, c: float) -> float:
    return float(pow(b, 2) - (4 * a * c))

def show_solution(a: float, b: float, d: float):
    if d < 0:
        print('no real solutions')
    else:
        x1, x2 = quadratic_formula(a, b, d)
        if d == 0:
            print(f'one solution: {x1:.5f}')
        else:
            print(f'two solutions: x1={x1:.5f} x2={x2:.5f}')

def quadratic_formula(a: float, b: float, d: float) -> tuple[float, float]:
    x_1 = (-b + sqrt(d)) / (2 * a)
    x_2 = (-b - sqrt(d)) / (2 * a)

    return tuple(sorted((x_1, x_2)))

def plot_quadratic(a: float, b: float, c: float, d: float):
    if d < 0:
        x_center = -b / (2 * a)

        x_min = x_center - 2
        x_max = x_center + 2
    else:
        x_1, x_2 = quadratic_formula(a, b, d)

        x_min = x_1 - 2
        x_max = x_2 + 2

    step = (x_max - x_min) / 149

    xs = [x_min + i * step for i in range(150)]
    ys = [a*pow(x, 2) + b*x + c for x in xs]

    plt.plot(xs, ys)
    plt.show()

def main():
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