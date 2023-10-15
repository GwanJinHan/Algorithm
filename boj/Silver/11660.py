import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

prefix = [[0] * (n + 1) for _ in range(n + 1)]
for r in range(1, n + 1):
    for c in range(1, n + 1):
        prefix[r][c] = prefix[r - 1][c] + prefix[r][c - 1] - \
            prefix[r - 1][c - 1] + arr[r - 1][c - 1]

ans = []
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans.append(prefix[x2][y2] - prefix[x1 - 1][y2] -
               prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1])

for a in ans:
    print(a)
