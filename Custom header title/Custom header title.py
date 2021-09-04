def transform_base(number, base, length):
    result = [0 for _ in range(length)]
    position = 1
    while number != 0:
        number, r = divmod(number, base)
        result[-position] = r
        position += 1

    return result


def solve(letters, n):
    result = ""
    number_of_options = len(letters)
    result_length = 1

    lower_boundary = 0
    upper_boundary = number_of_options - 1

    while True:
        if lower_boundary <= n <= upper_boundary:
            break
        else:
            result_length += 1
            lower_boundary = upper_boundary + 1
            upper_boundary = lower_boundary + number_of_options**result_length - 1

    remaining = n - lower_boundary
    indexes = transform_base(remaining, number_of_options, result_length)

    for index in indexes:
        result += letters[index]

    return result


def main():
    number_of_cases = int(input())
    for _ in range(number_of_cases):
        letters = input()
        n = int(input())
        print(solve(letters, n-1))


if __name__ == '__main__':
    main()
