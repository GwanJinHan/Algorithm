import sys
input = sys.stdin.readline

INF = sys.maxsize
v, e = map(int, input().split())
dp = [[INF] * v for _ in range(v)]

for i in range(v):
    dp[i][i] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    dp[a - 1][b - 1] = c

for inter in range(v):
    for r in range(v):
        for c in range(v):
            dp[r][c] = min(dp[r][c], dp[r][inter] + dp[inter][c])

ans = sys.maxsize
for i in range(v):
    for j in range(v):
        if i == j:
            continue
        ans = min(ans, dp[i][j] + dp[j][i])

print(-1 if ans == sys.maxsize else ans)
