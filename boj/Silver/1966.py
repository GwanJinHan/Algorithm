import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
ans = []
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    d = deque(arr)
    arr.sort()
    cnt = 0
    while True:
        t = d.popleft()
        if t != arr[-1]:
            d.append(t)
            if m == 0:
                m = len(d) - 1
            else:
                m -= 1
        else:
            arr.pop()
            cnt += 1
            if m == 0:
                break
            else:
                m -= 1

    ans.append(cnt)

for val in ans:
    print(val)
