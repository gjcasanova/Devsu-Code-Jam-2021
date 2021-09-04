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
