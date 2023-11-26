num = int(input())
dp = [1]

for cur in range(2, num + 1):
    if cur == (int(cur ** 0.5) ** 2):
        dp.append(1)
    else:
        dp.append(dp[cur - (int(cur ** 0.5) ** 2) - 1] + 1)

print(dp)
print(dp[-1])