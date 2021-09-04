def solve(text, subtext):
    index_a = text.find(subtext)
    index_b = text[::-1].find(subtext[::-1])

    text_length = len(text)
    subtext_length = len(subtext)

    if index_a == -1:
        return -1
    else:
        return min(index_a, text_length-subtext_length-index_a, index_b,
                   text_length-subtext_length-index_b)


def main():
    number_of_cases = int(input())
    for _ in range(number_of_cases):
        text = input()
        subtext = input()
        print(solve(text, subtext))


if __name__ == '__main__':
    main()
