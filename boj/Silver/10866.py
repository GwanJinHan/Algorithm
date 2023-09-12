from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d = deque()
for _ in range(n):
    c, *k = input().split()
    if k:
        k = int(*k)
    if c == "push_front":
        d.appendleft(k)
    elif c == "push_back":
        d.append(k)
    elif c == "pop_front":
        try:
            print(d.popleft())
        except:
            print(-1)
    elif c == "pop_back":
        try:
            print(d.pop())
        except:
            print(-1)
    elif c == "size":
        print(len(d))
    elif c == "empty":
        print(1 if len(d) == 0 else 0)
    elif c == "front":
        try:
            print(d[0])
        except:
            print(-1)
    elif c == "back":
        try:
            print(d[-1])
        except:
            print(-1)
