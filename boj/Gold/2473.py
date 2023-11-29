from bisect import bisect_left as bl
import sys

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left = 0
right = n - 1

ans_arr = []
ans = sys.maxsize

while left < right:
    t = arr[left] + arr[right]
    i = bl(arr, -t)

    while i >= right:
        i -= 1
    while i <= left:
        i += 1
    # i == n or i == 0: 값이 없다.
    # 0 < i < n : 1. i 에 해당하는 값 (target 값보다 같거나 큼) 2. i - 1에 있는 값. (target 보다 확실히 작음)
    if i != n and i != 0 and i != right and i != left:
        key = min(abs(t + arr[i]), abs(t + arr[i - 1]))
        if ans > key:
            if abs(t + arr[i]) > abs(t + arr[i - 1]) and i - 1 != left:
                ans = key
                ans_arr = [arr[left], arr[i - 1], arr[right]]
            # if abs(t + arr[i]) <= abs(t + arr[i - 1]) :
            else:
                ans = key
                ans_arr = [arr[left], arr[i], arr[right]]
        
    
    if t > 0:
        right -= 1
    elif t < 0:
        left += 1
    else:
        break
print(*ans_arr) 