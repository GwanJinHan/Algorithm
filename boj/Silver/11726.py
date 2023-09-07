from math import factorial as ft
n = int(input())

j = n % 2
cnt = 0
for i in range((n + 1) // 2, n + 1):
    cnt += (ft(i) // ft(j) // ft(i - j))
    j += 2

print(cnt % 10007)
