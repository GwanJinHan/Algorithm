n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, n - 1
cur = sum(arr)
cnt = 0
while left <= right:
    if cur == s:
        cnt += 1
    if abs(s - cur + arr[left]) < abs(s - cur + arr[right]):
        cur -= arr[left]
        left += 1
    else:
        cur -= arr[right]
        right -= 1

print(cnt)
