import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    dq = [(val, i) for i, val in enumerate(arr)]
    tar = dq[m]
    cnt = 0
    while True:
        cnt += 1
        val = dq[0]
        if val == max(dq):
            dq.popleft()
            if val == tar:
                print(cnt)
                break
        else:
            dq.append(dq.popleft())