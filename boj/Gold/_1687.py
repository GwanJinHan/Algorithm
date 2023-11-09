import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [
    list(map(int, list(input().rstrip()))) for _ in range(n)
]

prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j -
                                                                1] + arr[i - 1][j - 1] - prefix_sum[i - 1][j - 1]
ans = -1
for r in range(1, n + 1):
    for c in range(1, m + 1):
        if prefix_sum[r][c] == 0:
            ans = max(ans, r * c)

for p in prefix_sum:
    print(*p)
print(ans)
