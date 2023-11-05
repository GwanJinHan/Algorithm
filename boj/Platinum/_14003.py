from bisect import bisect_left as bl

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
d = [-1000000001]

for i in range(1, n + 1):
    idx = bl(d, arr[i])
    if idx == len(d):
        d.append(arr[i])
        dp[i] = idx
    elif idx == 0:
        d[0] = arr[i]
        dp[i] = 1
    else:
        if d[idx] == arr[i]:
            dp[i] = idx
        else:
            d[idx] = min(d[idx], arr[i])
            dp[i] = idx

print(len(d) - 1)
print(*d[1:])
