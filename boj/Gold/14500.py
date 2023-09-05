import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [
    list(map(int, input().split())) for _ in range(n)
]

answer = 0

for r in range(n):
    for c in range(m):
        temp = []
        # ㅡ
        if c + 3 < m:
            temp.append(sum(arr[r][c:c+4]))
        # |
        if r + 3 < n:
            temp.append(sum([val[c] for val in arr[r:r+4]]))

        # ㅁ
        if r + 1 < n and c + 1 < m:
            temp.append(sum(
                [arr[i][j] for i in range(r, r + 2) for j in range(c, c + 2)]))

        # 2 3
        if r + 1 < n and c + 2 < m:
            temp += [
                sum([arr[r][c+1], arr[r+1][c], arr[r+1][c+1], arr[r+1][c+2]]),
                sum([arr[r][c], arr[r][c+1], arr[r][c+2], arr[r+1][c+1]]),
                sum([arr[r][c+1], arr[r][c+2], arr[r+1][c], arr[r+1][c+1]]),
                sum([arr[r][c], arr[r][c+1], arr[r+1][c+1], arr[r+1][c+2]]),
                sum([arr[r][c], arr[r][c+1], arr[r][c+2], arr[r+1][c+2]]),
                sum([arr[r][c], arr[r+1][c], arr[r+1][c+1], arr[r+1][c+2]]),
                sum([arr[r][c], arr[r][c+1], arr[r][c+2], arr[r+1][c]]),
                sum([arr[r][c+2], arr[r+1][c], arr[r+1][c+1], arr[r+1][c+2]]),
            ]

        # 3 2
        if r + 2 < n and c + 1 < m:
            temp += [
                sum([arr[r][c], arr[r+1][c], arr[r+1][c+1], arr[r+2][c]]),
                sum([arr[r][c+1], arr[r+1][c], arr[r+1][c+1], arr[r+2][c+1]]),
                sum([arr[r][c+1], arr[r+1][c], arr[r+1][c+1], arr[r+2][c]]),
                sum([arr[r][c], arr[r+1][c], arr[r+1][c+1], arr[r+2][c+1]]),
                sum([arr[r][c], arr[r][c+1], arr[r+1][c], arr[r+2][c]]),
                sum([arr[r][c+1], arr[r+1][c+1], arr[r+2][c], arr[r+2][c+1]]),
                sum([arr[r][c], arr[r+1][c], arr[r+2][c], arr[r+2][c+1]]),
                sum([arr[r][c], arr[r][c+1], arr[r+1][c+1],  arr[r+2][c+1]]),
            ]

        answer = max([answer, *temp])
print(answer)
