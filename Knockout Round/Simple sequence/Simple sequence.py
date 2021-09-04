"""
Consider the following sequence: 1, 2, 3, 4, 3, 4, 5, 6, 5, 6, 7, 8, …
Given a number n that represents the nth number in the sequence, return the corresponding element
in the sequence
"""


def solve(n):
    group, position = divmod(n, 4)
    return 2*group+1+position


def main():
    number_of_cases = int(input())
    for _ in range(number_of_cases):
        n = int(input())
        print(solve(n-1))


if __name__ == '__main__':
    main()
