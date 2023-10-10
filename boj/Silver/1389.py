import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())

    arr[a - 1][b - 1] = 1
    arr[b - 1][a - 1] = 1

for inter in range(n):
    for r in range(n):
        for c in range(n):
            if inter == r or inter == c or r == c:
                continue

            if arr[r][inter] != 0 and arr[inter][c] != 0:
                if arr[r][c] == 0:
                    arr[r][c] = arr[r][inter] + arr[inter][c]
                else:
                    arr[r][c] = min(arr[r][c], arr[r][inter] + arr[inter][c])

ans = sys.maxsize
for val in arr:
    ans = min(sum(val), ans)

for i, val in enumerate(arr):
    if sum(val) == ans:
        print(i + 1)
        break
