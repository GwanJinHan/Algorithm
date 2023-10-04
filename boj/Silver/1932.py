import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0, *t, 0] for t in arr]
for i in range(1, len(arr)):
    for j in range(1, i + 2):
        dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[-1]))
