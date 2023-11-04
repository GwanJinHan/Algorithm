import sys
from collections import deque

n, k = map(int, input().split())

arr = [sys.maxsize] * 100002

queue = deque([(0, n)])  # 시간, 현위치

if n == k:
    queue = False
    arr[k] = 0

while queue:
    t, l = queue.popleft()

    if arr[l] < t:
        continue

    if l + 1 < 100002 and t + 1 < arr[l + 1]:
        arr[l + 1] = t + 1
        queue.append((arr[l + 1], l + 1))
    if 0 <= l - 1 and t + 1 < arr[l - 1]:
        arr[l - 1] = t + 1
        queue.append((arr[l - 1], l - 1))
    if l * 2 < 100002 and t < arr[l * 2]:
        arr[l * 2] = t
        queue.append((arr[l * 2], l * 2))

print(arr[k])
