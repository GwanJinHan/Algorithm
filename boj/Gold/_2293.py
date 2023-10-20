import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [
    int(input()) for _ in range(n)
]

coins.sort()

arr = [0] * (k + 1)

for coin in coins:
    cur = coin
    cnt = 1

    while cur <= k:
        arr[cur] = cnt
        cur += coin
        cnt += 1

ans = sys.maxsize
for i in range(k, k // 2, -1):
    if i == k:
        pass
    elif arr[k - i] == 0 or arr[i] == 0:
        continue
    ans = min(ans, arr[i] + arr[k - i])

if k % 2 == 0 and arr[k // 2] != 0:
    ans = min(arr[k // 2] * 2, ans)

print(ans if ans != sys.maxsize else -1)

# 0을 처리하자. 앞에서 가면서 0, 0 아니면 갱신하고 break
