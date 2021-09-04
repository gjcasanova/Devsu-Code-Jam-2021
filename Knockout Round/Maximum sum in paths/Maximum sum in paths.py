"""
Given a rectangular matrix of integers m, consider all the paths starting from the top right
to the bottom left corner and return the maximum sum of numbers among all paths. You can only
move in two directions: left or down.
"""


def solve(matrix):
    row = (len(matrix[0])+1) * [-10000]
    dp = [row.copy() for _ in range(len(matrix)+1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            if i == 1 and j == 1:
                dp[i][j] = matrix[i-1][j-1]
            elif i == 1:
                dp[i][j] = matrix[i-1][j-1] + dp[i][j-1]
            elif j == 1:
                dp[i][j] = matrix[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = matrix[i-1][j-1]+max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


def main():
    number_of_cases = int(input())
    for _ in range(number_of_cases):
        matrix = []
        input_as_text = input().replace(' ', '')

        for sub in input_as_text[2:len(input_as_text)-2].split('],['):
            row = []
            for element in sub.split(','):
                row.append(int(element))
            row.reverse()
            matrix.append(row)
        print(solve(matrix))


if __name__ == '__main__':
    main()
