"""David Evra - Homework 1, Problem 2: Pythagorean Numbers."""


def find_Pythagorean(n: int) -> list[tuple]:
    # Stores tuples that satisfies Pythagorean theorem.
    possible_pythagoreans = []

    # Checks all possible combination from a, b, and c from 1 through n.
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                if a**2 + b**2 == c**2:
                    possible_pythagoreans.append((a, b, c))

    return possible_pythagoreans

def main():
    n = int(input("Enter a positive integer limit: "))
    print(find_Pythagorean(n))

if __name__ == "__main__":
    main()