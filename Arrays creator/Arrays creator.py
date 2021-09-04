def solve(size, u):
    def search(variation, size, u):
        if len(variation) == size:
            return 1

        result = 0
        for element in range(u):
            if not (len(variation) >= 2 and variation[-1] == variation[-2] == element):
                variation.append(element)
                result += search(variation, size, u)
                variation.pop(-1)
        return result

    return search([], size, u)


def main():
    number_of_cases = int(input())
    for _ in range(number_of_cases):
        size = int(input())
        u = int(input())
        print(solve(size, u))


if __name__ == '__main__':
    main()
