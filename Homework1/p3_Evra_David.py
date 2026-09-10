"""David Evra - Homework 1, Problem 3: Duplicated Substrings."""

def find_dup_str(s, n):
    for i in range(len(s) - n + 1):
        init_str = s[i : i + n]

        for j in range(i + n, len(s) - n + 1):
            sec_str = s[j : j + n]

            if init_str == sec_str:
                return init_str
            
    return ""

def main():
    s = input("Enter string: ")
    n = int(input("Enter substring length: "))

    print(find_dup_str(s, n))

if __name__ == "__main__":
    main()
