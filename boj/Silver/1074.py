n, r, c = map(int, input().split())


root = [[0, 1], [2, 3]]


def Z(i, stacked, r, c):
    if i == 1:
        return root[r][c] + stacked

    if r < 2 ** (i - 1) and c < 2 ** (i - 1):
        pass
    elif r < 2 ** (i - 1) and c >= 2 ** (i - 1):
        c -= 2 ** (i - 1)
        stacked += (4 ** (i - 1)) * 1
    elif r >= 2 ** (i - 1) and c < 2 ** (i - 1):
        r -= 2 ** (i - 1)
        stacked += (4 ** (i - 1)) * 2
    elif r >= 2 ** (i - 1) and c >= 2 ** (i - 1):
        r -= 2 ** (i - 1)
        c -= 2 ** (i - 1)
        stacked += (4 ** (i - 1)) * 3

    return Z(i - 1, stacked, r, c)


print(Z(n, 0, r, c))
