"""
Given a text and a subText that might be in the text, return the minimum distance
from the subText to any side of the text. If the subText is not in the text, return -1.
The distance is the number of characters from the subText to any of the text sides.
"""


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
