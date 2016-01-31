#!/usr/bin/env python3

def LCS(str1, str2):

    m = len(str1)
    n = len(str2)

    array = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                array[i][j] = array[i-1][j-1] + 1
            else:
                array[i][j] = max(array[i-1][j],array[i][j-1])

    substr = backtrack(str1, str2, array, m, n)

    return array[m][n], substr


def backtrack(str1, str2, array, i, j):
    if i == 0 or j == 0:
        return ""
    elif str1[i-1] == str2[j-1]:
        return backtrack(str1, str2, array, i-1, j-1) + str1[i-1]
    elif array[i][j-1] > array[i-1][j]:
        return backtrack(str1, str2, array, i, j-1)
    else:
        return backtrack(str1, str2, array, i-1, j)


def main():
    str1 = 'abcbdab'
    str2 = 'bdcaba'

    c, substr = LCS(str1, str2)

    print(c, substr)

if __name__ == '__main__':
    main()
