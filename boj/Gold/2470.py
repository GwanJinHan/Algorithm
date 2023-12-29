n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = n - 1
k = 2000000001
ans = []

while left < right:
    t = arr[left] + arr[right]
    if abs(t) < k:
        ans = [arr[left], arr[right]]
        k = abs(t)
    if t == 0:
        break
    elif t > 0:
        right -= 1
    else:
        left += 1


print(*ans)
