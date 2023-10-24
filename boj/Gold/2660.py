import sys
input = sys.stdin.readline

n = int(input())

arr = [[0] * n for _ in range(n)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    arr[a - 1][b - 1] = 1
    arr[b - 1][a - 1] = 1

for inter in range(n):
    for r in range(n):
        for c in range(n):
            if r == c:
                continue

            if arr[r][inter] > 0 and arr[inter][c] > 0:
                if arr[r][c] == 0:
                    arr[r][c] = arr[r][inter] + arr[inter][c]
                else:
                    arr[r][c] = min(arr[r][c], arr[r][inter] + arr[inter][c])

min_val = sys.maxsize
for val in arr:
    min_val = min(min_val, max(val))

ans = []
for i, val in enumerate(arr):
    if max(val) == min_val:
        ans.append(i + 1)

print(min_val, len(ans))
print(*ans)
