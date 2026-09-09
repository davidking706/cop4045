"""David Evra - Homework 1, Problem 1: Quadratic Equations."""


def get_variable(v: str) -> float | None:
    vStr = input(f"Enter {v}: ")
    if vStr == "":
        return None

    return float(vStr)

def discriminant(a: float, b: float, c: float) -> float:
    return float(pow(b, 2) - (4 * a * c))

def main():
    while True:
        a = get_variable('a')
        if a == None:
            break

        b = get_variable('b')
        c = get_variable('c')
        d = discriminant(a, b, c)

        print(d)


if __name__ == "__main__":
    main()