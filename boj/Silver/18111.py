import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
arr = []

MAX = 0
MIN = 500
for _ in range(n):
    t = list(map(int, input().split()))
    MAX = max(MAX, max(t))
    MIN = min(MIN, min(t))
    arr.append(t)

ans = sys.maxsize
ans_h = 500
for h in range(MIN, MAX + 1):
    t_time = 0
    t_b = b
    for r in range(n):
        for c in range(m):
            if arr[r][c] > h:
                t_time += (arr[r][c] - h) * 2
                t_b += (arr[r][c] - h)
            elif arr[r][c] < h:
                t_time += (h - arr[r][c])
                t_b -= (h - arr[r][c])
    if t_b >= 0 and ans >= t_time:
        ans = t_time
        ans_h = h

print(ans, ans_h)
