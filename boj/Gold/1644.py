n = int(input())


primes = [False, False] + [True] * (n - 1)
arr = []
for i in range(2, n + 1):
    if primes[i]:
        arr.append(i)
        j = 2
        while i * j <= n:
            primes[i * j] = False
            j += 1

start = end = 0
cur = arr[0] if len(arr) != 0 else 0
ans = 0
while end < len(arr):
    if cur < n:
        end += 1
        if end >= len(arr):
            break
        cur += arr[end]
    elif cur > n:
        cur -= arr[start]
        start += 1
    else:
        ans += 1
        end += 1
        if end >= len(arr):
            break
        cur += arr[end]

print(ans)
