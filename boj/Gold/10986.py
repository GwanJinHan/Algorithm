n, m = map(int, input().split())
arr = list(map(int, input().split()))

acc = 0
prefix = [0] * n
mods = [0] * m
ans = 0

for i in range(n):
    acc += arr[i]
    prefix[i] = acc
    mods[acc % m] += 1
    if acc % m == 0:
        ans += 1


for i in range(m):
    if mods[i] < 2:
        continue
    ans += mods[i] * (mods[i] - 1) // 2

print(ans)
