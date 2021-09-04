def solve(numbers):
    results = []
    for number in numbers:
        results.append((sum([n for n in numbers if n != number]), number))

    results.sort(reverse=True)
    return results[0][1]


def main():
    number_of_cases = int(input())
    for _ in range(number_of_cases):
        input_as_text = input()
        input_as_text = input_as_text[1: len(input_as_text)-1]
        numbers = [int(i) for i in input_as_text.split(',')]
        print(solve(numbers))


if __name__ == '__main__':
    main()
