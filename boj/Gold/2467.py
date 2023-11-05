n = int(input())
arr = list(map(int, input().split()))
left, right = 0, n - 1

ans = 3000000000
a, b = 0, 0
while left < right:
    if abs(arr[right] + arr[left]) < ans:
        a, b = arr[left], arr[right]
        ans = abs(arr[right] + arr[left])

    if arr[right] + arr[left] > 0:
        right -= 1
    elif arr[right] + arr[left] < 0:
        left += 1
    else:
        break

print(a, b)
