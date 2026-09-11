"""David Evra - Homework 1, Problem 4: Function Visualization"""

import matplotlib.pyplot as plt
import math


def plot_function(fun_str, domain, ns):
    x_min, x_max = domain
    step = (x_max - x_min) / ns

    xs = [x_min + i * step for i in range(ns)]
    ys = [eval(fun_str) for x in xs]

    print("{:>10}{:>10}".format("x", "y"))
    print("-" * 20)

    for x, y in zip(xs, ys):
        print("{:10.4f}{:+10.4f}".format(x, y))

    plt.plot(xs, ys)
    plt.title(fun_str)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def main():
    # fun_str = "2 * math.sin(2*math.pi * x)"
    # ns = 100
    # x_min = -3.0
    # x_max = 3.0

    fun_str = input("Enter function with variable x: ")
    ns = int(input("Enter number of samples: "))
    x_min = float(input("Enter xmin: "))
    x_max = float(input("Enter xmax: "))

    plot_function(fun_str, (x_min, x_max), ns)

if __name__ == "__main__":
    main()
