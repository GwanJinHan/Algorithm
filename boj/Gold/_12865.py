import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

arr.sort(key=lambda x: x[0])

dp = [0] * (k + 1)

for w, v in arr:
    for i in range(w, k + 1):
        dp[i] = max(v + dp[k - i], dp[i], dp[i - 1])

print(max(dp))
